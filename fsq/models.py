from django.db import models

from django.utils.translation import gettext_lazy as _

COVID, ACTIVIYIES, DCT, DESERT_CAMPS, DUBAI_ASSURED, DUBAI_CALENDAR, DUBAI_EXPERT, DUBAI_WAY, \
EVENT_PERMITS, EVENT_SPONSORSHIP, EVENT_TICKETING, HOLIDAY_HOMES, HOTEL_CLASSIFICATION, \
HOTEL_MANAGEMENT, MEDYAF, EVENTS_DET, SAFARI_DRIVERS, SAFARIVEHICLES, SUPPLIERS, \
TOUR_GUIDES, TRADE_EVENTS = range(21)
TYPE = (
    (COVID, _('COVID'),),
    (ACTIVIYIES, _('ACTIVIYIES'),),
    (DCT, _('DCT'),),
    (DESERT_CAMPS, _('DESERT CAMPS'),),
    (DUBAI_ASSURED, _('DUBAI ASSURED'),),
    (DUBAI_CALENDAR, _('DUBAI CALENDAR'),),
    (DUBAI_EXPERT, _('DUBAI EXPERT'),),
    (DUBAI_WAY, _('DUBAI WAY'),),
    (EVENT_PERMITS, _('EVENT PERMITS'),),
    (EVENT_SPONSORSHIP, _('EVENT SPONSORSHIP'),),
    (EVENT_TICKETING, _('EVENT TICKETING'),),
    (HOLIDAY_HOMES, _('HOLIDAY HOMES'),),
    (HOTEL_CLASSIFICATION, _('HOTEL CLASSIFICATION'),),
    (HOTEL_MANAGEMENT, _('HOTEL MANAGEMENT'),),
    (MEDYAF, _('MEDYAF'),),
    (EVENTS_DET, _('EVENTS DET'),),
    (SAFARI_DRIVERS, _('SAFARI DRIVERS'),),
    (SAFARIVEHICLES, _('SAFARIVEHICLES'),),
    (SUPPLIERS, _('SUPPLIERS'),),
    (TOUR_GUIDES, _('TOUR GUIDES'),),
    (TRADE_EVENTS, _('TRADE EVENTS'),),

)

BOOLEAN_MODEL, EXTENDED_BOOLEAN_MODEL, VECTOR_MODEL = range(3)
PROBLEM_TYPE = (
    (BOOLEAN_MODEL, _('BOOLEAN MODEL'),),
    (EXTENDED_BOOLEAN_MODEL, _('EXTENDED BOOLEAN MODEL'),),
    (VECTOR_MODEL, _('VECTOR MODEL'),),
)


class Faq(models.Model):
    question = models.TextField(db_index=True)
    answer = models.TextField(db_index=True)
    type = models.PositiveSmallIntegerField(verbose_name=_('type'),
                                            choices=TYPE,
                                            default=COVID,
                                            db_index=True, )

    def __str__(self):
        return f"Question {self.pk}"


class Problem(models.Model):
    question = models.TextField()
    type = models.PositiveSmallIntegerField(verbose_name=_('Algorithm Type'),
                                            choices=PROBLEM_TYPE,
                                            default=BOOLEAN_MODEL,
                                            )

    def __str__(self):
        return f"The Question number that Entered by the user is{self.pk}"


