const imgTrigger = document.querySelectorAll('.img-trigger');


imgTrigger.forEach(function (img) {
    img.addEventListener('click', function () {
        const imgModal = img.getAttribute('data-trigger');
        document.getElementById(imgModal).classList.add('open');
        document.getElementById(imgModal).addEventListener("click", function (e) {
            if (e.target.classList.contains('modal')) {
                document.getElementById(imgModal).classList.remove('open')
            }
        });
        const imgSrc = img.getAttribute('data-image');
        const modalImg = document.querySelector('.modal-img');
        modalImg.src = `${imgSrc}`
    })
});

