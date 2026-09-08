const search = document.getElementById('search');
const type = document.getElementById('type');
const cards = [...document.querySelectorAll('.card')];
function filterArtwork() {
  const query = search.value.toLowerCase().trim();
  let visible = 0;
  for (const card of cards) {
    card.hidden = !card.dataset.search.includes(query) || (type.value !== '' && card.dataset.type !== type.value);
    if (!card.hidden) visible += 1;
  }
  for (const section of document.querySelectorAll('.update')) {
    section.hidden = !section.querySelector('.card:not([hidden])');
  }
  document.getElementById('count').textContent = `${visible} of ${cards.length} images`;
  document.getElementById('empty').hidden = visible !== 0;
}
search.addEventListener('input', filterArtwork);
type.addEventListener('change', filterArtwork);
filterArtwork();
