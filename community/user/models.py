from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='이메일', default='test@gmail.com')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registared_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    # class has no objects member 에러 제거용
    objects = models.Manager()

    # 새로 추가한 user의 data가 object형태로 나오는 부분 수정
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'community_user'
        verbose_name = '게시판 사용자' 
        verbose_name_plural = '게시판 사용자'