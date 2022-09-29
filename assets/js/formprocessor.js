'use strict';
const resetForm =form =>{  
    form.reset(0); 
    const file =form.querySelector("[type=file]");  
    const fileLabel =form.querySelector('#filename'); 
    file?file.files=new DataTransfer().files: null; 
    fileLabel?fileLabel.textContent =' No file chosen' :null;
}

const serializeForm =async (form)=>{ 
    const formData ={}; const radioFields =[] 
    for (const field of [...form.querySelectorAll('input, select, textarea')]) {
        const {name, value, disabled} =field;  

        if(!name || disabled) return;   
        formData[name] =value; 
    }     
    return  JSON.stringify({...formData}); 
} 

const postForm =async evt =>{
    evt.preventDefault(); 
    const {target} =evt;
    const {action, method} =target  
    const formData =await serializeForm(target); 
    const {csrf_token} = JSON.parse(formData);  

    $.ajaxSetup({ beforeSend: (xhr, settings) => {if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) xhr.setRequestHeader("X-CSRFToken", csrf_token)}});
    $.ajax({ 
        url:action,
        type: method,
        data: formData,
        contentType: 'application/json',  
        dataType: 'json',
        success: data => processResponse(data),
        error: error =>  processResponse(error) 
    });  
} 

const processResponse = response =>{
    console.log(response);
}

const freezeCtaButton =button =>{
    // const resetButton = () => {button.removeAttribute('disabled'); 
    // button.textContent =defaultText};  

    // const button =target.querySelector(dataCta);
    // button.setAttribute('disabled', true); 
    // const defaultText =button.textContent;
    // const parts =label !=''?label.split(' '): button.textContent.split(' ');
    // let [verb, noun] =parts.length >1?parts: [...parts, '']; 
    // verb =verb.toLowerCase()[verb.length-1] =='e'?verb.split('').slice(0,verb.length-1).join(''):verb;
    // button.textContent =`${verb}ing ${noun}...`;
    console.log(button);
}