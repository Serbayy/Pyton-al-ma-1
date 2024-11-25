## ÖDEV 1 ##

 ## Virtual Enviromment Oluşturma ##

Görev 1: Kendi isminizle bir virtual environment  oluşturunuz, oluşturma esnasında Pyhton 3 kurulumu
 yapınız.

## Cevap: Conda create -n sadıkenv python=3
## conda env list ( Bütün env. görebilirsiniz. )

## Görev 2: Oluşturduğunuzenvironment'ıaktifediniz.

## Cevap: conda activate sadıkenv

## Görev 3:  Yüklüp aketleri listeleyiniz.

## Cevap:   conda list

## Görev 4:  Environment içerisineNumpy'ıngüncelversiyonunuvePandas'ın1.2.1 versiyonunuaynıandaindiriniz.

## Cevap:   conda install Numpy Pandas=1.2.1

## Görev 5:  İndirilenNumpy'ınversiyonunedir?

## Cevap:   conda list  (versiyon 1.21.5)

## Görev 6:  Pandas'ıupgrade ediniz. Yeni versiyonunedir?

## Cevap: conda upgrade pandas
##   conda list

## Görev 7:  Numpy'ıenvironment'tansiliniz.

## Cevap: conda remove Numpy

## Görev 8: Seaborn ve natpolitlib kütüphanelerinin güncel versiyonlarını aynı anda indiriniz.
## Cevap: Conda install seaborn matpolitlib

## Görev 9:   Virtual environment içindeki  kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.

## Cevap: conda env export > environment.yaml

Görev 10:  Oluşturduğunuz environment'i siliniz. Önce environment' i deactive ediniz.

## Cevap: conda deactivate
conda env remove -n sadık