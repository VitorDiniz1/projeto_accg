(function(win,doc){
    'use strict';
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel')
        for(let i =0; i<btnDel.length;i++){
            btnDel[i].addEventListener('click',function(event){
                if(confirm('Deseja mesmo apagar os dados?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            })
        }
    }
})(window,document);