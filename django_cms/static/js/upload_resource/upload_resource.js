/**
 * Created by Administrator on 2017/10/16.
 */
function upload_resource(url,title,uploaded_type,id,type,post_name,name_type){
    if(post_name==null||post_name==''){
        post_name=id;
    }
    if(name_type==null||name_type==''||name_type==1){
        name_type=1;
    }
    else{
        name_type=2;
    }
    var now_num=$('#'+id).children().length;

    layer.open({
        title: title,
        type: 2,
        area: ['800px', '480px'],
        fix: true, //固定
        maxmin: false,
        move: false,
        resize: false,
        zIndex: 100000,
        content: url+"?post_name="+post_name
    });
}

function cropper_upload(title,id,post_name,width,height){
    var url = CROPPER_RESOURCE_URL+"/" + id+"/"+post_name+"/"+width+"/"+height;
    layer.open({
        title: title,
        type: 2,
        area: ['1000px', '600px'],
        fix: true, //固定
        maxmin: false,
        move: false,
        resize: false,
        zIndex: 100000,
        content: url
    });
}

function del_img($this){
    //console.log($(this));
    $this.parent().remove();
}