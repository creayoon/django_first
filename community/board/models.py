from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer  = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='작성자')
    registared_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    # class has no objects member 에러 제거용
    objects = models.Manager()

    # 새로 추가한 user의 data가 object형태로 나오는 부 분 수정
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'community_board'
        verbose_name = '게시글'  
        verbose_name_plural = '게시글'