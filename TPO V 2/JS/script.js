const scriptURL = 'https://script.google.com/macros/s/AKfycbxeSb2vyBylGqsgbqbbeBSOWZo6NYtiulXPvKL7GFwPH-kc2r7D1TxZiHboPTNu11JI/exec'
const form = document.forms['submit-form']

form.addEventListener('submit', e => {
  e.preventDefault()
  fetch(scriptURL, { method: 'POST', body: new FormData(form)})
    .then(response => console.log('Success!', response))
    .catch(error => console.error('Error!', error.message))
})