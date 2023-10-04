'use strict';
// all the buttons
const student_login = document.querySelector('.student');
const admin = document.querySelector('.admin');
const parent = document.querySelector('.parent')

const login_form = document.querySelector('.for-form');
const cancelicon = document.querySelector('.cancel-icon');
const featuressec = document.querySelector('.features-sec');
const login_sec = document.querySelector('.login-sec');
const section_edit = document.querySelector('.section-edit');
const login_admin =document.querySelector('.for-form-admin');
const login_parent = document.querySelector('.for-form-parent')
const canceladminicon = document.querySelector('.canceladminicon')
const cancelparenticon = document.querySelector('.cancelparenticon')
const create_btn = document.querySelector('.creatBtn')
const create_query_block = document.querySelector('.create-popup');

create_btn.addEventListener("click", function(e){
    e.preventDefault();
    create_query_block.style.display = "block"
    console.log("clicked")

})

parent.addEventListener("click", function (e) {
    // Prevent form from submitting
    e.preventDefault();
    login_parent.style.display = "block"
    featuressec.style.filter="blur(5px)"
    login_sec.style.filter="blur(5px)"
    section_edit.style.filter="blur(5px)"
       
});
cancelparenticon.addEventListener("click",function (e){
    login_parent.style.display = "none"
    featuressec.style.filter="none"
    login_sec.style.filter="none"
    section_edit.style.filter="none"

});

admin.addEventListener("click", function (e) {
    // Prevent form from submitting
    e.preventDefault();
    login_admin.style.display = "block"
    featuressec.style.filter="blur(5px)"
    login_sec.style.filter="blur(5px)"
    section_edit.style.filter="blur(5px)"
       
});
canceladminicon.addEventListener("click",function (e){
    login_admin.style.display = "none"
    featuressec.style.filter="none"
    login_sec.style.filter="none"
    section_edit.style.filter="none"

});


student_login.addEventListener("click", function (e) {
    // Prevent form from submitting
    e.preventDefault();
    login_form.style.display = "block"
    featuressec.style.filter="blur(5px)"
    login_sec.style.filter="blur(5px)"
    section_edit.style.filter="blur(5px)"
    
    
});
cancelicon.addEventListener("click",function (e){
    login_form.style.display = "none"
    featuressec.style.filter="none"
    login_sec.style.filter="none"
    section_edit.style.filter="none"

});