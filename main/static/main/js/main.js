function deleteAsteriskFields(){
    document.querySelectorAll('.asteriskField').forEach((item)=>{
        item.remove()
    })
}
function leftSmallUl(){
    document.getElementById('hint_id_password1').querySelector('ul').style.paddingLeft = '0';
}

function itemFormRow ()
{
   const a = document.getElementById('add_car')
   if (a) {
    a.querySelectorAll('.form-group').forEach((item)=>{
        item.classList.add('mx-3')
    })
   }
}

function clicks(){
    alert('Успешно добавлено!')
}

function edit_form(){
    alert('Успешно изменено')
}


