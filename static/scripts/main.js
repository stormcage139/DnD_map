window.canBeDragged = true // Для отслеживания , можно ли перетаскивать карту (например = false,когда открыта инфа о местности)


class zoneDescription{
	tooltip = document.querySelector('.tooltip');

	// continents = document.querySelectorAll('.continent');
	// continentred = document.querySelectorAll('.continentred');
	// continentbl = document.querySelectorAll('.continentbl');

	popupBg = document.querySelector('.info__bg');
	popup__photo = document.querySelector('.info__photo');
	popup__title = document.querySelector('.info__title');
	popup__text = document.querySelector('.info__text');
	
	more__info = document.querySelector('.info__link')

	zoneElements = document.getElementById("map__zones")

 	selectors = [".continent",".continentred",".continentbl"]

	pushmenuElement = document.querySelector("#nav-icon3")
	
	
	constructor(){
		this.bindEvents()
	}

	pushmenuFunction = function() {
		document.body.style.cursor = 'default'
		document.querySelector('.pushmenu').classList.toggle('open');
		document.querySelector('.sidebar').classList.toggle('show');
		document.querySelector('.hidden-overley').classList.toggle('show');
		document.body.classList.toggle('sidebar-opened')
		// if (!document.querySelector('.pushmenu').classList.contains('open')) {window.canBeDragged = true} else {window.canBeDragged = false} ; хз потом переделаю(должно запрещать перемещать карту при открытом боковом окне(панели))
	};

	showDescription(target){
		document.body.style.cursor = 'default'
		if (window.wantToDrag){ 
			window.canBeDragged = false; //Проверка через глобальную переменную
			this.popup__title.textContent = target.getAttribute('data-title');
			this.popup__photo.setAttribute('src', target.getAttribute('data-photo'));
			this.popup__text.textContent = target.getAttribute('data-description');
			this.popupBg.classList.add('active');
			this.more__info.setAttribute('href',target.getAttribute('more-info'))
			this.more__info.textContent = 'Подробнее о ' + target.getAttribute('data-title')
		} 

		
	}

	// truncateDescription(description, maxSentences = 3) {
	// 	let sentences = description.split(".");
	// 	if (sentences.length > maxSentences) {
	// 		return sentences.slice(0, maxSentences).join(".") + "....";
	// 	}
	// 	return description;
	// }


	bindEvents(){
		this.zoneElements.addEventListener('click', (event) => {
			console.log(event)
			// console.log(this.selectors.some(selector => event.target.matches(selector)))
			if (event.target.matches(this.selectors)) { //Оно не должно работать тк matches не принимает,но работает,да и ладно
				// console.log(true)
				this.showDescription(event.target)
		}})

		document.addEventListener('click', (event) => {
			if(event.target === this.popupBg) {
				this.popupBg.classList.remove('active');
				window.canBeDragged = true
			}
		});

		this.pushmenuElement.addEventListener('click', this.pushmenuFunction, false);

		document.addEventListener('DOMContentLoaded', () => {

			// получаем все элементы с классом pushmenu
			const pushmenu = document.getElementsByClassName('pushmenu');
			
			// получаем элемент с классом hidden-overley
			const hiddenOverley = document.querySelector('.hidden-overley');
		
			// отслеживаем клик клика по оверлею
			hiddenOverley.addEventListener('click', (event) => {
				
				event.currentTarget.classList.toggle('show');
				document.querySelector('.sidebar').classList.toggle('show');
				document.querySelector('body').classList.toggle('sidebar-opened');
				for( i=0; i < pushmenu.length; i++ ){
						pushmenu[i].classList.toggle('open');
				}
			});
		
			
		
		
			// Отслеживаем клики кнопок с классом pushmenu (Я черт его знает зачем тут цикл(тут одна итерация),я переписал,ошибки будут, тогда верну)
			// for( i=0; i < pushmenu.length; i++ ){
			// 	console.log(pushmenu[i])
			// 	pushmenu[i].addEventListener('click', pushmenuFunction, false);
			// }
		
			// Получим все родительские элементы в меню
			const sidebarAccordeon = document.querySelectorAll('.sidebar .menu-parent-item a:first-child');
			const accordeonFunction =  function() { 
				this.parentNode.querySelector('ul').classList.toggle('show');
				this.querySelector('i').classList.toggle('rotate');
			}
			// Отслеживаем клики родительских пунктов меню 
			for(let i=0; i < sidebarAccordeon.length; i++ ){
				sidebarAccordeon[i].addEventListener('click', accordeonFunction, false);
			}
			
		});
	}
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


		// Заменил н делегирования ивента родительскому блоку выше
		// continents.forEach((item) => {
		//     item.addEventListener('click', showDescription);
		// });

		// continentred.forEach((item) => {
		//     item.addEventListener('click', showDescription);
		// });

		// continentbl.forEach((item) => {
		//     item.addEventListener('click', showDescription);
		// });






class mapDragger{
	clientXposition = 0
	clientYposition = 0
	isDragging = false;
	startX = 0 
	startY = 0 
	scrollLeft = 0
	scrollTop = 0
	constructor(){
		this.bindEvents()
	}
	bindEvents(){
		document.body.addEventListener('mousedown', (e) => {
			this.clientXposition = e.clientX
			this.clientYposition = e.clientY
			if (e.button === 0) { // Проверяем, что нажата левая кнопка мыши
				this.isDragging = true;
				this.startX = e.clientX; // Используем clientX вместо pageX
				this.startY = e.clientY; // Используем clientY вместо pageY
				this.scrollLeft = window.scrollX;
				this.scrollTop = window.scrollY;
				document.body.style.cursor = 'grabbing';
				document.body.style.userSelect = 'none'; // Отключаем выделение текста при перетаскивании
				e.preventDefault(); // Предотвращаем стандартное поведение
			}
		});

		document.body.addEventListener('mousemove', (e) => {
			if (!this.isDragging || !window.canBeDragged) return;
			const x = e.clientX - this.startX;
			const y = e.clientY - this.startY;
			window.scrollTo(this.scrollLeft - x, this.scrollTop - y);
			e.preventDefault(); // Предотвращаем стандартное поведение
		});

		document.body.addEventListener('mouseup', (e) => {
			window.wantToDrag = (this.clientXposition === e.clientX && this.clientYposition === e.clientY)
			this.isDragging = false;
			document.body.style.cursor = 'grab';
			document.body.style.userSelect = ''; // Восстанавливаем выделение текста
		});

		document.body.addEventListener('mouseleave', () => {
			this.isDragging = false;
			document.body.style.cursor = 'grab';
			document.body.style.userSelect = ''; // Восстанавливаем выделение текста
		});
	}
}

new zoneDescription()
new mapDragger()