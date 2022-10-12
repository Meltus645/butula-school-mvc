'use strict'; 
 
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
}
 
const promptDelete =async (self, item) =>{
    const {dataset} =self;
    if(!confirm(`Are you sure to delete ${item}?\nThis action cannot be undone!`)) return;
    const delete_response =await request(dataset.uri);
    if(delete_response.ok){
        const {deleted, detail} =await delete_response.json()
        if (deleted) activateTab(document.getElementById('list'));
        else alert(detail);
    }
    
}