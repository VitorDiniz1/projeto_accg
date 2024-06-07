
function backTop(){
    window.scrollTo({
        top:0,
        behavior:'smooth'
    })
}

ScrollReveal({
    reset:true,
    distance:"60px",
    duration:4000,
    delay:400
})

ScrollReveal().reveal('.container-sessao',{delay:400,origin:'bottom',duration:2000})