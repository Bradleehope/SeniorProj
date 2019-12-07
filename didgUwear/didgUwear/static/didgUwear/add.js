function addNewShirt(){
    nickname = $('#nickname').val();
    primary_color = $('#primary_color').val();
    style = $('#style').val();
    secondary_color = $('#secondary_color').val();
    occasion = $('#occation').val();
    weather = $('#weather').val();
    pattern = $('#pattern').val();
    holiday = $('#holiday').val();
    description = $('#description').val();
    brand = $('#brand').val();
    img_link = $('#img_link').val();

    $.getJson("{{ url('didgUwear:addinputshirt', nickname='NICK_PH', primary_color='PC_PH', style='STYLE_PH', secondary_color='SC_PH', occation='OCC_PH', weather='WE_PH', pattern='PAT_PH', holiday='HOLI_PH', description='DESC_PH', brand='BRAND_PH', img_link='IMG_PH')}} ".replace(
        'NICK_PH', nickname).replace('PC_PH', primary_color).replace('STYLE_PH', style).replace('SC_PH', secondary_color).replace(
        'OCC_PH', occation).replace('WE_PH', weather).replace('PAT_PH', pattern).replace('HOLI_PH', holiday).replace(
        'DESC_PH', description).replace('BRAND_PH', brand).replace('IMG_PH', img_link), updatePage);
}

function updatePage(data){
    console.log(data);
    location.reload();
}