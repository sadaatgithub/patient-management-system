from rest_framework_nested import routers
from . import views
from django.urls import path
from pprint import pprint



router = routers.DefaultRouter()
router.register('api/home', views.HomeViewSet, basename="home")
# patient_visit_router = routers.NestedDefaultRouter(router,'api/home',lookup="patient_id")
# patient_visit_router.register('visit',views.EachPatientVisitViewSet, basename="patient-visit")

router.register('api/visits', views.PatientVisitView, basename="visits")
router.register('api/appointments', views.AppointmentViewSet, basename="appointment")
router.register('api/prescription', views.PrescriptionViewSet, basename="prescription")
router.register('api/doctor', views.DoctorViewSet, basename="doctor")
# router.register('api/all', views.SingleApiView, basename="all")


# pprint(router.urls)
# urlpatterns = router.urls 
urlpatterns = [
    path('auth/jwt/create/', views.CustomTokenObtainPairView.as_view()),
    path('auth/jwt/refresh/', views.CustomTokenRefreshView.as_view()),
    path('auth/jwt/verify/', views.CustomTokenVerifyView.as_view()),

] + router.urls 