#coding:utf-8
class Singletion:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_sgl'):
            cls._sgl = super().__new__(cls,*args,**kwargs)
        return cls._sgl
