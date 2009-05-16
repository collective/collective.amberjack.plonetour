AjStep = function(type,jq,value){
	this._JQ = jq;
	this._TYPE = type;
	this._VALUE = value;
}
AjStep.prototype = {
	getJq: function(){
		return this._JQ;
	},
	getType: function(){
		return this._TYPE;
	},
	getValue: function(){
		return this._VALUE;
	},
	getObj: function(){
		var type_obj = this._TYPE;
		if(this._JQ=='')return jq(AjStandardSteps[this._TYPE]);
		else return jq(this._JQ);
	},
}

/**
 * Utility function that prepare the page for the tour
 * @author Massimo Azzolini
 * @author Giacomo Spettoli
 */
function ajTour(){
	/* 
	 * sets the plone elements that can be "pressed" as "highlight"
	 * next we need to alert the user if he tries to click somewhere else..
	 */
	
	var theAJClass = 'ajHighlight';
	var theAJClassBehavoiur = 'ajedElement';
	
	jq('.' + theAJClassBehavoiur).click(function(){
		Amberjack.createCookie('ajcookie_tourId', Amberjack.tourId, 1);
		Amberjack.createCookie('ajcookie_skinId', Amberjack.skinId, 1);
	});
	
	// manages the << >> buttons
	var ajNext = jq('#ajNext');
	var ajPrev = jq('#ajPrev');
	
	ajNext.click(function(){
		if (Amberjack.pageId == 2) {
			return false;
		}
	});
}

/**
 * Function for disabling all links that can break the tour.
 * @author Giacomo Spettoli
 */
function disableLinks(){
	if(Amberjack.pageId){
		var notAj = jq("button, input, textarea, select, a").not(".ajHighlight,.ajedElement,[id^='aj'],[class^='aj']");
		//NOTA: non ci devono essere elementi estranei con id che comincia con aj
		notAj.click(function(){
			alert("For close the tour please use the console's button");
			return false;
		});
		notAj.keypress(function(){
			alert("For close the tour please use the console's button");
			return false;
		});
		notAj.css("color", "#CCCCCC");
		notAj.css("cursor", "default");

		var ajClose = jq("#ajClose");
		var goHome = false;
		
		var sURL = unescape(window.location.pathname);
		if(goHome)
			ajClose.attr("onClick","Amberjack.close();location.href='" + Amberjack.BASE_URL + "';return false");
		else
			ajClose.attr("onClick","Amberjack.close();location.href = window.location.pathname;return false");

		var ajNext = jq("#ajNext");
		ajNext.attr("onClick","if(checkAllStep()){" + ajNext.attr('onClick') + "}");
	}
}

/**
 * Get all current page's step
 * @author Giacomo Spettoli
 * @return steps array of current page step's id
 */
function getPageSteps(){
	var steps = [];
	if(Amberjack.pageId){
		var link = jq(Amberjack.pages[Amberjack.pageId].content ).children('a[class^="ajStep"]');
		link.each(function(i){
			var allClasses = jq(this).attr('class').split(' ');
			var firstClass = allClasses[0].split('-');
			steps.push(firstClass[1]);
		});
	}
	return steps;
}


/**
 * Highlight the step for better view
 * @author Giacomo Spettoli
 * 
 * @param num dictionary's label of the step
 */
function highlightStep(num){
	if(Amberjack.pageId){
		
		var theAJClass = 'ajHighlight';
		var theAJClassBehaviour = 'ajedElement';
		var obj;
		try{
			obj = AjSteps[num].getObj();
		}catch(e){
			alert("Error in highlightStep(): Step " + num +" not found");
			return false;
		}
		var type_obj = AjSteps[num].getType();
		
		if(type_obj=="checkbox" || type_obj=="radio"){
			jq("label[for="+obj.attr('id')+"]").addClass(theAJClass);
			obj.addClass(theAJClassBehaviour);
		}
		else if (type_obj=="select"){
			var highlightThis = jq(obj + " option[value="+ AjSteps[num].getValue() +"]");
			highlightThis.addClass(theAJClass);
			obj.addClass(theAJClassBehaviour);
		}
		else if (type_obj=="multiple_select"){
			var tmp = AjSteps[num].getValue().split(",");
			for (var i=0;i<tmp.length;i++){
				jq("option[value="+tmp[i]+"]").addClass(theAJClass);
			}
			obj.addClass(theAJClassBehaviour);
		}
		else if (type_obj.match("menu")){
			obj.addClass(theAJClass);
			obj.children('dt').children('a').addClass(theAJClassBehaviour);
		}
		else{
			obj.addClass(theAJClass);
			obj.addClass(theAJClassBehaviour);
		}
	}
}

/**
 * Highlight all current page's steps
 * @author Giacomo Spettoli
 */
function highlightAllStep(){
	var steps = getPageSteps();
	for(i =0; i < steps.length;i++){
		highlightStep(steps[i]);
	}
}

function switchClass(obj,remClass,addClass){
	obj.removeClass(remClass);
	obj.addClass(addClass);
}

/**
 * Change the value of a textbox
 * @author Giacomo Spettoli
 *
 * @param obj object to modify
 * @param value new value of the object
 */
function changeValue(obj,value){
	obj.focus();
	//obj.click();
	obj.val(value);
	obj.blur();
}

/**
 * Function for doing steps
 * @author Giacomo Spettoli
 * 
 * @param num dictionary's label of the step
 */
function doStep(step){
	var obj,type_obj,jq_obj,value;
	
	var allClasses = jq(step).attr("class").split(" ");
	var firstClass = allClasses[0].split('-');
	var num = firstClass[1];

	try{
		obj = AjSteps[num].getObj();
		type_obj = AjSteps[num].getType();
		jq_obj = AjSteps[num].getJq();
		value = AjSteps[num].getValue();
	}catch(e){
		alert("Error in doStep(): Step " + num +" not found");
		return false;
	}
	//alert('DoStep: Jq=' + jq_obj +'\nType='+type_obj+'\nValue='+value + '\n Obj=' + obj.text());

	if(type_obj == 'link') location.href = obj.attr('href') + "?tourId=p4aTour&skinId=safari";
	else if(type_obj == 'button') obj.click();
	else if(type_obj == 'collapsible'){
		if(value=='collapse') switchClass(obj, 'expandedInlineCollapsible', 'collapsedInlineCollapsible');
		else switchClass(obj, 'collapsedInlineCollapsible', 'expandedInlineCollapsible');
	}
	else if(type_obj == "select" || type_obj == "text")	changeValue(obj,value);
	else if(type_obj == "checkbox" || type_obj == "radio"){
		if(value=='checked')obj.attr('checked',value);
		else obj.removeAttr('checked');
	}
	else if(type_obj == "multiple_select"){
		var tmp = value.split(",");
		for (var i=0;i<tmp.length;i++){
			jq("option[value="+tmp[i]+"]").attr("selected","selected");
		}
	}
	else if(type_obj=="form_save_new" || type_obj=="form_save"){
		var form = obj.parents("form")
		form.submit(function(){
			Amberjack.createCookie('ajcookie_tourId', Amberjack.tourId, 1);
			Amberjack.createCookie('ajcookie_skinId', Amberjack.skinId, 1);
		});
		form.submit()
	}
	// STANDARD STEPS
	else if(type_obj.match("menu")){
		if(value=='deactivate') switchClass(obj, 'activated', 'deactivated');
		else switchClass(obj,'deactivated','activated');
	}
	else if(value!=""){
		changeValue(obj,value);
	}
	else if(jq_obj==""){
		obj.click(function(){
			Amberjack.createCookie('ajcookie_tourId', Amberjack.tourId, 1);
			Amberjack.createCookie('ajcookie_skinId', Amberjack.skinId, 1);
		});	
		obj.click();
		if(obj.attr("href"))
			location.href = obj.attr("href");
	}	
}

/**
 * Check that the step has been done.
 * @author Giacomo Spettoli
 *  
 * @param num dictionary's label of the step
 * @return true if done else false
 */
function checkStep(num){
	var obj;
	try{
		obj = AjSteps[num].getObj();
	}catch(e){
		alert("Error in checkStep(): Step " + num +" not found");
		return false;
	}
	
	var type_obj = AjSteps[num].getType();
	var value = AjSteps[num].getValue();
	var stepDone = false;
	if(type_obj == "collapsible"){
		if(value=="collapse") {
			stepDone = obj.hasClass("collapsedInlineCollapsible");
		}
		else stepDone = obj.hasClass("expandedInlineCollapsible");
	}
	else if(type_obj == "checkbox" || type_obj == "radio") stepDone = obj.attr("checked");
	else if(type_obj == "select" || type_obj == "text") stepDone = (obj.val()==value?true:false);
	return stepDone;
}

/**
 * Check all current page's steps
 * @author Giacomo Spettoli
 * 
 * @return true if all steps done else false
 */
function checkAllStep(){
	var allDone = true;
	var thisStep = true;

    var steps = getPageSteps();
    for(i =0; i < steps.length;i++){
		thisStep = checkStep(steps[i]);
		if(!thisStep){
			alert("Step "+steps[i]+" not completed");
			allDone = false;
			break;
		}
		allDone = allDone && thisStep;
	}	
	return allDone;
}

/**
 * Start the tour and set some timeout
 * @author Giacomo Spettoli
 */
registerPloneFunction(function () {
	openAmberjack();
	setTimeout("highlightAllStep()", 300);
	setTimeout("ajTour()", 400);
	setTimeout("disableLinks()", 500);
})