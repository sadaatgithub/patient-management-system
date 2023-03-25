from rest_framework_nested import routers
from . import views
from pprint import pprint



router = routers.DefaultRouter()
router.register('api/home', views.HomeViewSet, basename="home")
# patient_visit_router = routers.NestedDefaultRouter(router,'api/home',lookup="patient_id")
# patient_visit_router.register('visit',views.EachPatientVisitViewSet, basename="patient-visit")

router.register('api/visits', views.PatientVisitView, basename="visits")
router.register('api/appointments', views.AppointmentViewSet, basename="appointment")
router.register('api/prescription', views.PrescriptionViewSet, basename="prescription")
# router.register('api/all', views.SingleApiView, basename="all")


# pprint(router.urls)
urlpatterns = router.urls 