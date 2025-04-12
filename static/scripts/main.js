let continents = document.querySelectorAll('.continent');
let continentred = document.querySelectorAll('.continentred');
let continentbl = document.querySelectorAll('.continentbl');
let popupBg = document.querySelector('.info__bg');
let popup__photo = document.querySelector('.info__photo');
let popup__title = document.querySelector('.info__title');
let popup__text = document.querySelector('.info__text');
let tooltip = document.querySelector('.tooltip');
let more__info = document.querySelector('.info__link')

function truncateDescription(description, maxSentences = 3) {
    let sentences = description.split(".");
    if (sentences.length > maxSentences) {
        return sentences.slice(0, maxSentences).join(".") + "....";
    }
    return description;
}

// item.addEventListener('mouseenter', function() {
    //     tooltip.textContent = item.getAttribute('data-title');
    //     tooltip.style.display = 'block';
    // });

    // item.addEventListener('mouseleave', function() {
    //     tooltip.textContent = item.getAttribute('data-title');
    //     tooltip.style.display = 'none';
    // });

    // item.addEventListener('mousemove', function(e) {
    //     tooltip.style.top = (e.y + 20) + 'px';
    //     tooltip.style.left = (e.x + 20) + 'px';
    // });

continents.forEach((item) => {
    item.addEventListener('click', function() {
        popup__title.textContent = this.getAttribute('data-title');
        popup__photo.setAttribute('src', this.getAttribute('data-photo'));
        popup__text.textContent = truncateDescription(this.getAttribute('data-description'));
        popupBg.classList.add('active');
		more__info.setAttribute('href',this.getAttribute('more-info'))
		more__info.textContent = 'Подробнее о ' + this.getAttribute('data-title') 
    });
});

continentred.forEach((item) => {
    item.addEventListener('click', function() {
        popup__title.textContent = this.getAttribute('data-title');
        popup__photo.setAttribute('src', this.getAttribute('data-photo'));
        popup__text.textContent = truncateDescription(this.getAttribute('data-description'));
        popupBg.classList.add('active');
		more__info.setAttribute('href',this.getAttribute('more-info'))
		more__info.textContent = 'Подробнее о ' + this.getAttribute('data-title') 
    });
});

continentbl.forEach((item) => {
    item.addEventListener('click', function() {
        popup__title.textContent = this.getAttribute('data-title');
        popup__photo.setAttribute('src', this.getAttribute('data-photo'));
        popup__text.textContent = truncateDescription(this.getAttribute('data-description'));
        popupBg.classList.add('active');
		more__info.setAttribute('href',this.getAttribute('more-info'))
		more__info.textContent = 'Подробнее о ' + this.getAttribute('data-title') 
    });
});


document.addEventListener('click', (e) => {
    if(e.target === popupBg) {
        popupBg.classList.remove('active');
    }
});

document.addEventListener('DOMContentLoaded', () => {

	// получаем все элементы с классом pushmenu
	const pushmenu = document.getElementsByClassName('pushmenu');

	// получаем элемент с классом hidden-overley
	const hiddenOverley = document.querySelector('.hidden-overley');

	// отслеживаем клик клика по оверлею
	hiddenOverley.addEventListener('click', (e) => {
		e.currentTarget.classList.toggle('show');
		document.querySelector('.sidebar').classList.toggle('show');
		document.querySelector('body').classList.toggle('sidebar-opened');
		for( i=0; i < pushmenu.length; i++ ){
				pushmenu[i].classList.toggle('open');
		}
	});

	const pushmenuFunction = function() {
		document.querySelector('.pushmenu').classList.toggle('open');
		document.querySelector('.sidebar').classList.toggle('show');
		document.querySelector('.hidden-overley').classList.toggle('show');
		document.body.classList.toggle('sidebar-opened')
	};

	// Отслеживаем клики кнопок с классом pushmenu 
	for( i=0; i < pushmenu.length; i++ ){
		pushmenu[i].addEventListener('click', pushmenuFunction, false);
	}

	// Получим все родительские элементы в меню
	const sidebarAccordeon = document.querySelectorAll('.sidebar .menu-parent-item a:first-child');
	const accordeonFunction =  function() { 
		this.parentNode.querySelector('ul').classList.toggle('show');
		this.querySelector('i').classList.toggle('rotate');
	}
	// Отслеживаем клики родительских пунктов меню 
	for( i=0; i < sidebarAccordeon.length; i++ ){
		sidebarAccordeon[i].addEventListener('click', accordeonFunction, false);
	}
	
});
// let isDragging = false;
// let startX, startY, scrollLeft, scrollTop;

// document.body.addEventListener('mousedown', (e) => {
// 	if (e.button === 0) { // Проверяем, что нажата левая кнопка мыши
// 		isDragging = true;
// 		startX = e.pageX;
// 		startY = e.pageY;
// 		scrollLeft = window.scrollX;
// 		scrollTop = window.scrollY;
// 		document.body.style.cursor = 'grabbing';
// 	}
// });

// document.body.addEventListener('mousemove', (e) => {
// 	if (isDragging) {
// 		const x = e.pageX - startX;
// 		const y = e.pageY - startY;
// 		window.scrollTo(scrollLeft - x, scrollTop - y);
// 	}
// });

// document.body.addEventListener('mouseup', () => {
// 	isDragging = false;
// 	document.body.style.cursor = 'grab';
// });

// document.body.addEventListener('mouseleave', () => {
// 	isDragging = false;
// 	document.body.style.cursor = 'grab';
// });