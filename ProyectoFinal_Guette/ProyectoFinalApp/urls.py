from django.urls import path



from .views import *



urlpatterns = [
    
    
    
    
    path('usuario/nuevo',nuevo_usuario, name='crear_usuario' ),
    path('usuario/login',login_user, name='login' ),
    path ('', inicio, name="inicio"),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='users-profile'),
    path('about/', about, name='about'),
    # path('profile/images', profile, name='profile_images'),

    path('Sega/', Segas, name="Sega"),
    path('Sega/cargar_Sega/', crear_Sega , name="cargar_Sega"),
    path('eliminar_Sega/<Segas_id>', eliminar_Sega, name="eliminar_Sega"),
    path('editar_Sega/<Segas_id>', editar_Sega, name="editar_Sega"),

    path('Sega/list', SegaList.as_view(), name="Sega_list"),
    path(r'^(?P<pk>\d+)$', SegaDetail.as_view(), name="Sega_detail"),
    path(r'^nuevo$', SegaCreate.as_view(), name="Sega_create"),
    path(r'^editar/Sega/(?P<pk>\d+)$', SegaUpdate.as_view(), name="Sega_update"),
    path(r'^eliminar/Sega/(?P<pk>\d+)$', SegaDelete.as_view(), name="Sega_delete"),


    
    path('GameBoy/', GameBoys, name="GameBoy"),
    path('cargar_GameBoy/', crear_GameBoy , name="cargar_GameBoy"),
    path('eliminar_GameBoy/<GameBoy_id>', eliminar_GameBoy, name="eliminar_GameBoy"),
    path('editar_GameBoy/<GameBoy_id>', editar_GameBoy, name="editar_GameBoy"),

    
    path(r'GameBoy/list', GameBoyList.as_view(), name="GameBoy_list"),
    path(r'^(?P<pk>\d+)$', GameBoyDetail.as_view(), name="GameBoy_detail"),
    path(r'^nuevo$', GameBoyCreate.as_view(), name="GameBoy_create"),
    path(r'^editar/GameBoy(?P<pk>\d+)$', GameBoyUpdate.as_view(), name="GameBoy_update"),
    path(r'^eliminar/GameBoy(?P<pk>\d+)$', GameBoyDelete.as_view(), name="GameBoy_delete"),

    path('Nes/', Ness, name="Nes"),
    path(r'Nes/list', NesList.as_view(), name="Nes_list"),
    path('crear_Nes/', crear_Nes, name="crear_Nes"),
    path('eliminar_Nes/<Nes_id>/', eliminar_Nes, name="eliminar_Nes"),
    path('editar_Nes/<Nes_id>/', editar_Nes, name="editar_Nes"),
    
    path(r'Nes/list', NesList.as_view(), name="Nes_list"),
    path(r'^(?P<pk>\d+)$', NesDetail.as_view(), name="Nes_detail"),
    path(r'^nuevo$', NesCreate.as_view(), name="Nes_create"),
    path(r'^editar/Nes(?P<pk>\d+)$', NesUpdate.as_view(), name="Nes_update"),
    path(r'^eliminar/Nes(?P<pk>\d+)$', NesDelete.as_view(), name="Nes_delete"),
   
    
    
] 

    