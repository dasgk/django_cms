/**
 * Created by Administrator on 2017/10/16.
 */
 // url显示上传文件html页面的url
 // title 显示页面的标题
 // uploaded_type 上传的type_key
 //id 显示文件的div
 //type  2
 // post_name 表示的是
 // name_type 表示的是
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
        content: url+"?uploaded_type="+uploaded_type+"&file_id="+id
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