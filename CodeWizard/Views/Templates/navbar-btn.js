const template = document.createElement('template');
template.innerHTML = `
<div>
    <!--Healine-->
    <p>Rating</p>
    <!--rating-stars-->
    <div class="rating-stars">
        <div class="rating-star star-1"></div>
        <div class="rating-star star-2"></div>
        <div class="rating-star star-3"></div>
        <div class="rating-star star-4"></div>
        <div class="rating-star star-5"></div>
    </div>
</div>
`
export class Rating extends HTMLElement {
    constructor() {
        super();
    }
}

window.customElements.define('my-rating', Rating)
