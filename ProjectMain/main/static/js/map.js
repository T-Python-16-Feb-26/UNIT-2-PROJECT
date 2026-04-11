/**
 * Interactive Saudi Arabia province map for the wildlife class pages.
 *
 * Expects on the page:
 *   - #map-container  : div where the SVG is injected
 *   - #region-panel   : container shown after a region is clicked
 *   - #region-title   : h-tag updated with province name
 *   - #region-species : div filled with species mini-cards
 *   - window.PROVINCE_DATA : object of { province_slug: [{slug,name,scientific_name,image}, ...] }
 *   - window.MAP_SVG_URL   : URL to sa_map.svg static file
 */

// Province slug → SVG region id
const PROVINCE_TO_REGION = {
  'riyadh':           1,
  'makkah':           2,
  'mecca':            2,  // alias
  'madinah':          3,
  'qassim':           4,
  'eastern-province': 5,
  'asir':             6,
  'tabuk':            7,
  'hail':             8,
  'northern-borders': 9,
  'jizan':           10,
  'najran':          11,
  'bahah':           12,
  'jouf':            13,
};

// SVG region id → display name
const REGION_NAMES = {
  1:  'Riyadh',
  2:  'Makkah',
  3:  'Madinah',
  4:  'Qassim',
  5:  'Eastern Province',
  6:  'Asir',
  7:  'Tabuk',
  8:  'Hail',
  9:  'Northern Borders',
  10: 'Jizan',
  11: 'Najran',
  12: 'Bahah',
  13: 'Jouf',
};

// Build reverse map: region id → list of province slugs that map to it
function buildRegionToProvinces() {
  const r2p = {};
  for (const [slug, id] of Object.entries(PROVINCE_TO_REGION)) {
    if (!r2p[id]) r2p[id] = [];
    if (!r2p[id].includes(slug)) r2p[id].push(slug);
  }
  return r2p;
}

// Gather all species for a given region id from PROVINCE_DATA
function speciesForRegion(regionId, provinceData, regionToProvinces) {
  const provinces = regionToProvinces[regionId] || [];
  const seen = new Set();
  const result = [];
  for (const slug of provinces) {
    for (const sp of (provinceData[slug] || [])) {
      if (!seen.has(sp.slug)) {
        seen.add(sp.slug);
        result.push(sp);
      }
    }
  }
  return result;
}

// Determine which region ids have at least one species
function activeRegions(provinceData) {
  const active = new Set();
  for (const [slug, species] of Object.entries(provinceData)) {
    if (species.length > 0) {
      const id = PROVINCE_TO_REGION[slug];
      if (id !== undefined) active.add(id);
    }
  }
  return active;
}

function buildSpeciesCard(sp) {
  const imgHtml = sp.image
    ? `<img src="${sp.image}" alt="${sp.name}" class="region-species-img">`
    : `<div class="region-species-img region-species-img--placeholder"></div>`;
  return `
    <a href="/species/${sp.slug}/" class="region-species-card text-decoration-none">
      ${imgHtml}
      <div class="region-species-info">
        <div class="region-species-name">${sp.name}</div>
        <div class="region-species-sci">${sp.scientific_name}</div>
      </div>
    </a>`;
}

function initMap(svgText, provinceData) {
  const container = document.getElementById('map-container');
  if (!container) return;
  container.innerHTML = svgText;

  const regionToProvinces = buildRegionToProvinces();
  const active = activeRegions(provinceData);
  const paths = container.querySelectorAll('.sa-region');
  let selectedRegion = null;

  // Apply initial dim/active state
  paths.forEach(path => {
    const id = parseInt(path.dataset.region, 10);
    if (!active.has(id)) {
      path.classList.add('region-inactive');
    } else {
      path.classList.add('region-active');
    }
  });

  // Click handler
  paths.forEach(path => {
    const id = parseInt(path.dataset.region, 10);
    if (!active.has(id)) return;

    path.addEventListener('click', () => {
      // Deselect previous
      if (selectedRegion !== null) {
        const prev = container.querySelector(`[data-region="${selectedRegion}"]`);
        if (prev) prev.classList.remove('region-selected');
      }

      if (selectedRegion === id) {
        // Toggle off
        selectedRegion = null;
        hidePanel();
        return;
      }

      selectedRegion = id;
      path.classList.add('region-selected');

      const species = speciesForRegion(id, provinceData, regionToProvinces);
      showPanel(id, species);
    });

    path.style.cursor = 'pointer';
  });

  function showPanel(regionId, species) {
    const panel = document.getElementById('region-panel');
    const title = document.getElementById('region-title');
    const grid  = document.getElementById('region-species');
    if (!panel || !title || !grid) return;

    title.textContent = REGION_NAMES[regionId] || `Region ${regionId}`;
    grid.innerHTML = species.map(buildSpeciesCard).join('');
    panel.hidden = false;
    panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function hidePanel() {
    const panel = document.getElementById('region-panel');
    if (panel) panel.hidden = true;
  }
}

// Fetch SVG then initialise
document.addEventListener('DOMContentLoaded', () => {
  const provinceData = window.PROVINCE_DATA || {};
  const svgUrl = window.MAP_SVG_URL;
  if (!svgUrl) return;

  fetch(svgUrl)
    .then(r => r.text())
    .then(svgText => initMap(svgText, provinceData))
    .catch(err => console.warn('Map load failed:', err));
});
