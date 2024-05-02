let productImages = document.querySelectorAll('.preview-image');
let productImage = document.getElementById('product_image');

console.log(productImages)

productImages.forEach(function(element) {
    element.addEventListener('click', function() {
        let imgUrl = element.dataset.imgUrl;

        productImage.src = imgUrl;
        console.log(imgUrl);
    })
});