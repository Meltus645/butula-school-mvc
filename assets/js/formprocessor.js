'use strict';

const previewFile =(file, viewer) =>{
    const previeImage =self.querySelector('img'); 
    !file? viewer.setAttribute('src', '/assets/img/pp.jpg'):null;
    fileToBase64(fileList[0]).then(({file}) => previeImage.src =file).catch(error => alert(error)) 

}
const openFile = self =>{ // open file functionality  
    const file =document.forms[self.getAttribute('data-form')].querySelector(self.getAttribute('data-click')); file.click();  
    file.addEventListener('change',  ({target}) =>{
        self.removeAttribute('title');
        const fileList =target.files;
        if(fileList.length >0) {
            const filename = fileList[0].name && fileList[0].name !='' ? fileList[0].name: 'No file chosen'
            const fileLabel =target.parentNode.querySelector(file.getAttribute('data-file-label')); 
            if (filename.length <=15) fileLabel.textContent =filename;
            else{
                fileLabel.textContent =`${filename.slice(0,6)}...${filename.slice(filename.length-6,filename.length)}`;
                self.setAttribute('title', filename);
            }  
        } 
    })
}

const resetForm =form =>{  
    form.reset(0); 
    const file =form.querySelector("[type=file]");  
    const fileLabel =form.querySelector('#filename'); 
    file?file.files=new DataTransfer().files: null; 
    fileLabel?fileLabel.textContent =' No file chosen' :null;
}

 

const postForm =evt =>{
    evt.preventDefault(); 
    const {target} =evt;
    const {action, method} =target 
    const formData = new FormData(target); 
    // serialize multiselect field
    [...target.querySelectorAll('[multiple]')].forEach(({name, children}) =>{
        const choices =[];
        [...children].forEach(({selected, value}) =>selected?choices.push(value):null); 
        formData.set(name, JSON.stringify(choices));  // encode array to send it as a string  
    }); 
    $.ajaxSetup({ beforeSend: (xhr, settings) => {if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) xhr.setRequestHeader("X-CSRFToken", target.csrf_token.value)}}); // stackoverflow
    $.ajax({ 
        url:action,
        type: method,
        data: formData,
        contentType: false,  
        processData: false,
        cache: false,
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