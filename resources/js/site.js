import GLightbox from 'glightbox';
import 'glightbox/dist/css/glightbox.css';
import Glide from '@glidejs/glide'
import '@glidejs/glide/dist/css/glide.core.css';
import '@glidejs/glide/dist/css/glide.theme.css';

const lightbox = GLightbox();
new Glide('.glide', {
	type: 'carousel',
	autoplay: 5000,
	animationDuration: 1500,
}).mount();
