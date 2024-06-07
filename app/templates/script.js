let sections = document.querySelectorAll('section')
let navLinks = document.querySelectorAll('header nav a')


window.onscroll = () =>{
    sections.forEach(sec =>{
        let top = window.scrollY
        let offset = sec.offsetTop - 100
        let height = sec.offsetHeight
        let id = sec.getAttribute('id')

        if(top >= offset && top < offset + height){
            navLinks.forEach(links =>{
                links.classList.remove('active')
                document.querySelector('header nav a[href*='+ id  + ']').classList.add('active')
            })
        }
    })
}


function menuShow(){
    let menuMobile = document.querySelector('.mobile-menu')
    if(menuMobile.classList.contains('open')){
        menuMobile.classList.remove('open')
    }else{
        menuMobile.classList.add('open')
    }
}


ScrollReveal({
    reset:true,
    distance:"60px",
    duration:4000,
    delay:400
})

ScrollReveal().reveal('.div-text h2',{delay:400,origin:'left',duration:1000})

ScrollReveal().reveal('.div-btn',{delay:400,origin:'bottom',duration:2000})

ScrollReveal().reveal('.div-cao',{delay:400,origin:'bottom',duration:2000})

ScrollReveal().reveal('h1',{delay:400,origin:'left',duration:1000})

ScrollReveal().reveal('h3',{delay:400,origin:'left',duration:1000})

ScrollReveal().reveal('.select-row',{delay:400,origin:'bottom',duration:2000})

ScrollReveal().reveal('.fotos-animais',{delay:400,origin:'bottom',duration:2000})

ScrollReveal().reveal('.help-row',{delay:400,origin:'bottom',duration:2000})

ScrollReveal().reveal('.about-fundo',{delay:400,origin:'bottom',duration:2000})

let count = 1 

document.getElementById('radio1').checked = true

setInterval(function(){
    nextImage()


},3000)

function nextImage(){
    count++
    if(count>4){
        count= 1
    }

    document.getElementById('radio'+count).checked = true
}