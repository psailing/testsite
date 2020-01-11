$(function () {
	$('.book').click(function () {
		$('#modal').addClass('show');
	});
	$('.modal2__overlay').click(function() {
		$('#modal').removeClass('show')
	})
})

$(document).ready(function() { // Ждём загрузки страницы

	$(".food").click(function(){	// Событие клика на маленькое изображение
	  	var img = $(this);	// Получаем изображение, на которое кликнули
		var src = img.attr('src'); // Достаем из этого изображения путь до картинки
		$("body").append("<div class='popup'>"+ //Добавляем в тело документа разметку всплывающего окна
						 "<div class='popup_bg'></div>"+ // Блок, который будет служить фоном затемненным
						 "<img src='"+src+"' class='popup_img' />"+ // Само увеличенное фото
						 "</div>");
		$(".popup").fadeIn(400); // Медленно выводим изображение
		$(".popup_bg").click(function(){	// Событие клика на затемненный фон
			$(".popup").fadeOut(400);	// Медленно убираем всплывающее окно
			setTimeout(function() {	// Выставляем таймер
			  $(".popup").remove(); // Удаляем разметку всплывающего окна
			}, 400);
		});
	});

});