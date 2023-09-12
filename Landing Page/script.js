function chengeFormSelectorValue(value){
		
	document.querySelectorAll('.form-select option').forEach(element => {
		element.removeAttribute('selected')
	});
	
	document.getElementById(value).setAttribute('selected','selected');
	
}

function sendData(){
	
	if(
	(document.getElementById('validationCustom01').value.length > 0) &&
	(document.getElementById('validationCustom02').value.length > 0) &&
	(document.getElementById('validationCustomUsername').value.length> 0)
	){
		if( document.getElementById( 'checkboxs').checked ){
			alert("Данные отправленны, мы скоро свяжемся с вами!");
		}else{
			alert("Данные не отправленны, примите условия!");
		}
	}
}