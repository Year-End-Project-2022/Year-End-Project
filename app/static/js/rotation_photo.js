function randomNumber(min, max) {
  return Math.random() * (max - min) + min;
}

const elements = document.querySelectorAll('.galerie');
Array.from(elements).forEach((element, index) => {
	var number = randomNumber(-8, 8);
	$(element).css("transform", "rotate(" + number + "deg)");
	console.log(number);
});
