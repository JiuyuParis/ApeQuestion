$(document).ready(function(){
    //获取验证码按钮点击事件
    sendRegisterCapture()
});

//发送邮箱验证码函数
function sendRegisterCapture(){
    //发送验证码按钮点击事件
    $('#captureButton').on('click',function (){
        //将$('#captureButton')赋值给变量
        let $this=$(this);
        let email=$("input[name='email']").val();
            $.ajax({
                url:'/user/capture',
                data:{
                    email:email
                },
                success:function (result){
                    if(result.code===200){
                        alert(result.message);
                        $this.off('click');
                        //60秒后允许重新发送
                        let seconds=60;
                        let timer=setInterval(()=>{
                            seconds-=1;
                            if(seconds>0){
                                $this.text(seconds+'秒后重新发送');
                            }else{
                                $this.text('获取验证码');
                                //一定要停止计时器计时
                                clearInterval(timer);
                                sendRegisterCapture();
                            }
                        },1000)
                    }else if(result.code===500){
                        alert(result.message)
                    }
                }
            })
    })
}