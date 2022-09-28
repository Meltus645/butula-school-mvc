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

const activateTab = async (self, page) =>{
    const {parentNode, dataset} =self;
    const root_url =`http://localhost:8080/admin/${page}`  
    for(const node of parentNode.children) node.classList.contains('active') && node !== self? node.classList.remove('active'): self.classList.add('active');
    
    const endpoint =`${root_url}${dataset.uri}`
    history.pushState('', '', endpoint)
    const response =await request(`${endpoint}?init=app`);  

    if(response.ok) document.querySelector('#tabContent').innerHTML =await response.text(); 
}
 