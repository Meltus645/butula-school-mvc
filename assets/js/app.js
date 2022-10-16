'use strict'; 

const dataSets ={ subjects: [] }; 
const selectableContainer =createElement('div',); 
const selectedContainer =createElement('ul', {'class': 'd-flex btn-select'});
const request =async (endpoint, method ='GET', data=null, csrf_token=null)  =>{
    let options ={};
    let response;
    if(method !='GET' && csrf_token && data){
        options ={
            method,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRF-Token': csrf_token
            },
            body: JSON.stringify(data)
        }
    }
    try {response =fetch(endpoint, options);}
    catch ({message}) {response =message;} 
    finally{return response;}
};  

const activateTab = async self =>{  
    const {parentNode, dataset} =self;  
    for(const node of parentNode.children) node.classList.contains('active') && node !== self? node.classList.remove('active'): self.classList.add('active');
    let {uri} =dataset 
    history.pushState('', '', uri);
    uri =/\?[a-zA-Z]+=/gi.test(uri)?`${uri}&init=app` :`${uri}?init=app`
    const response =await request(uri);  
    if(response.ok) document.querySelector('#tabContent').innerHTML =await response.text();  
};
 
const promptDelete =async (self, item) =>{
    const {dataset} =self;
    if(!confirm(`Are you sure to delete ${item}?\nThis action cannot be undone!`)) return;
    const delete_response =await request(dataset.uri);
    if(delete_response.ok){
        const {deleted, detail} =await delete_response.json()
        if (deleted) activateTab(document.getElementById('list'));
        else alert(detail);
    }
    
};

const modalPop = async self =>{
    const {uri, parent} =self.dataset;
    const response =await request(uri); 
    const parentElement =document.querySelector(parent); 
    let popup =parentElement.querySelector('#popup');
    if(!popup){ 
        popup =document.createElement('div');
        popup.classList.add('popup');
        popup.id ="popup";
        parentElement.appendChild(popup);
    }
    if(popup){ 
        popup.innerHTML =await response.text();  
        $('#staticBackdrop').modal('show');
        [...popup.querySelectorAll('[data-dismiss=modal]')].forEach(modal => modal.addEventListener('click', () =>{
            parentElement.removeChild(popup)
        }, false));
    } 
    subjectSelection(parentElement);
};

function subjectSelection(parent){
    const content =parent.querySelector('[data-content=subjects]');  
    const parentNode =content.parentNode; 
    dataSets.subjects =JSON.parse(content.value);  
    filterSubjects();

    // create child element
    const optionsDisplay =createElement('div');
    const input =createElement('input', {name: 'subjects', type: 'hidden', value: content.value});   
    
    // append to parent element/node
    optionsDisplay.appendChild(selectedContainer);
    optionsDisplay.appendChild(selectableContainer);
    optionsDisplay.appendChild(input);
    parentNode.appendChild(optionsDisplay);
    
}  

function toggleItemSelection (self){
    const {item} =self.dataset;
    dataSets.subjects.forEach(subject =>{if(subject.id ==item && subject.type =='Optional') subject.selected =!subject.selected}) 
    filterSubjects();
} 

const filterSubjects = ()=>{
    selectableContainer.innerHTML ='';
    selectedContainer.innerHTML ='';
     
   const departments ={}; 
    dataSets.subjects.forEach(subject=> {
        if(subject.selected) {selectedContainer.innerHTML =`${selectedContainer.innerHTML}<li><button type ="button" data-item ="${subject.id}" data-item-selected ="${subject.selected}" onclick ="toggleItemSelection(this)" data-selectable ="${subject.type =='Optional'}">${subject.name}</button></li>`} 
        else{ 
            departments[subject.department] =departments[subject.department]?departments[subject.department]:[]
            departments[subject.department] =[...departments[subject.department],`<li><button type ="button" data-item ="${subject.id}" data-item-selected ="${subject.selected}" onclick ="toggleItemSelection(this)" data-selectable ="true">${subject.name}</button></li>`];
        }
    });  
    selectableContainer.innerHTML =[...Object.keys(departments)].map(department_key =>{ 
        return ` 
            <h3>${department_key}</h3> 
            <ul class ="d-flex btn-select">
                ${departments[department_key].join('')}
            </ul> 
        `
    }).join(''); 
};

function createElement (name, properties={}){
    const element =document.createElement(name);
    for(const property of Object.keys(properties)) element.setAttribute(property, properties[property]);
    return element;
} 

const submitForm =self =>{
    const {cta} =self.dataset; 
    document.getElementById(cta).click(); 
}