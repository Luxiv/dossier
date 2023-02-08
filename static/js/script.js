

const langlist = document.querySelectorAll('.lang-item');
langlist.forEach(item => {
  item.addEventListener('click', (e) => {
    langlist.forEach(el => { el.classList.remove('lang-item--active'); });
    item.classList.add('lang-item--active');
  });
});

const jobIcoList = document.querySelectorAll('.job-ico');
jobIcoList.forEach(item => {
  item.addEventListener('click', () => {
    jobIcoList.forEach(el => { el.classList.remove('job-ico--active'); });
    item.classList.add('job-ico--active');
  });
});

const paymentList = document.querySelectorAll('.patient-log_payment');
paymentList.forEach(item => {
  if (item.innerHTML == 0) {
    console.log('0');
    item.parentElement.classList.add('patient-log_payment-zero');
  }
  item.innerHTML += 'грн';
});

const patiensListAllItem = document.querySelectorAll('.patiens-list-all-item');
patiensListAllItem.forEach(item => {
  item.addEventListener('click', () => {
    patiensListAllItem.forEach(el => {
      el.classList.remove('patiens-list-all-item-btns--visible');
    });
    item.classList.add('patiens-list-all-item-btns--visible');
  });
});



const formAddRadioLang = document.querySelector('.form-add_radio-lang');
formAddRadioLang.addEventListener('click', () => {
  const add_radio_lang_ru = document.querySelector('#radio-lang-ru');
  const add_radio_lang_x = document.querySelector('#radio-lang-x');
  const add_radio_lang_UA = document.querySelector('#radio-lang-UA');
  if (add_radio_lang_ru.checked) {
    console.log('checked');
    add_radio_lang_ru.parentElement.style = 'color: #0f0';
    add_radio_lang_x.parentElement.style = 'color: #fff';
    add_radio_lang_UA.parentElement.style = 'color: #fff';
  }
  if (add_radio_lang_x.checked) {
    console.log('checked');
    add_radio_lang_ru.parentElement.style = 'color: #fff';
    add_radio_lang_x.parentElement.style = 'color: #0f0';
    add_radio_lang_UA.parentElement.style = 'color: #fff';
  }
  if (add_radio_lang_UA.checked) {
    console.log('checked');
    add_radio_lang_ru.parentElement.style = 'color: #fff';
    add_radio_lang_x.parentElement.style = 'color: #fff';
    add_radio_lang_UA.parentElement.style = 'color: #0f0';
  }
});



// const formAddRadioPA = document.querySelector('.form-add_radio-p-a');
// const radioPAChair = document.querySelector('#radio-p-a-chair');
// const radioPAWalk = document.querySelector('#radio-p-a-walkr');
// const radioPABarbell = document.querySelector('#radio-p-a-barbell');
  
// formAddRadioPA.addEventListener('click', (e) => {
//   if (radioPAChair.checked) {

//   }
// })



