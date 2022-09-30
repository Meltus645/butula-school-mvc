(() =>{
    'use strict';
    let d =document, i=new Image,e=encodeURIComponent; 
    const canvas =d.createElement('canvas'); 
    const context =canvas.getContext('2d'); 
    const text = 'i9asdm..$po((^@KbXrww!cz';
    context.textBaseline ='top';
    context.font =`16px 'Arial'`;
    context.textBaseline ='alphabetic';
    context.rotate(.05);
    context.fillStyle ='#f60'; 
    context.fillRect (125, 1, 62, 20);
    context.fillStyle ='#069';  
    context.fillText(text, 2, 15);
    context.fillStyle ='rgba(102, 200, 0, 0.7)';
    context.fillText(text, 4, 17);
    context.shadowblur =10;
    context.shadowColor ='blue';
    context.fillRect(-20, 10, 234,5); 
    const string  =canvas.toDataURL();
    let hash =0;
    if(string.length >0) {
        for(let i =0; i <string.length; i++){
            let char =string.charCodeAt(i);
            hash =((hash<<5) -hash)+char;
            hash =hash & hash;
        }  
        i.src='%s/a.gif?url='+e(d.location.pathname)+'&ref='+e(d.referrer)+'&code='+e(hash);
    }})();