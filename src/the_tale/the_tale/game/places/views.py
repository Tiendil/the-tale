
import smart_imports

smart_imports.all()


########################################
# processors definition
########################################
class PlaceProcessor(dext_views.ArgumentProcessor):
    def parse(self, context, raw_value):
        try:
            place_id = int(raw_value)
        except ValueError:
            self.raise_wrong_format()

        place = storage.places.get(place_id)

        if not place:
            self.raise_wrong_value()

        return place


########################################
# resource and global processors
########################################
resource = dext_views.Resource(name='places')
resource.add_processor(accounts_views.CurrentAccountProcessor())
resource.add_processor(utils_views.FakeResourceProcessor())


########################################
# views
########################################
@utils_api.Processor(versions=(conf.settings.API_LIST_VERSION,))
@resource('api', 'list', name='api-list')
def api_list(context):
    data = {'places': {}}

    for place in storage.places.all():
        place_data = {'name': place.name,
                      'id': place.id,
                      'frontier': place.is_frontier,
                      'position': {'x': place.x,
                                   'y': place.y},
                      'size': place.attrs.size,
                      'specialization': place._modifier.value}
        data['places'][place.id] = place_data

    return dext_views.AjaxOk(content=utils_api.olbanize(data))


@utils_api.Processor(versions=(conf.settings.API_SHOW_VERSION,))
@PlaceProcessor(error_message='Город не найден', url_name='place', context_name='place')
@resource('#place', 'api', 'show', name='api-show')
def api_show(context):
    return dext_views.AjaxOk(content=utils_api.olbanize(info.place_info(context.place, full_building_info=context.api_version != '2.0')))


@PlaceProcessor(error_message='Город не найден', url_name='place', context_name='place')
@resource('#place', name='show')
def show(context):

    inner_circle = politic_power_logic.get_inner_circle(place_id=context.place.id)

    accounts_short_infos = game_short_info.get_accounts_accounts_info(inner_circle.heroes_ids())

    job_power = politic_power_logic.get_job_power(place_id=context.place.id)

    persons_inner_circles = {person.id: politic_power_logic.get_inner_circle(person_id=person.id)
                             for person in context.place.persons}

    total_events, events = chronicle_tt_services.chronicle.cmd_get_last_events(tags=[context.place.meta_object().tag],
                                                                               number=conf.settings.CHRONICLE_RECORDS_NUMBER)

    tt_api_events_log.fill_events_wtih_meta_objects(events)

    return dext_views.Page('places/show.html',
                           content={'place': context.place,
                                    'place_bills': info.place_info_bills(context.place),
                                    'place_chronicle': events,
                                    'accounts_short_infos': accounts_short_infos,
                                    'inner_circle': inner_circle,
                                    'persons_inner_circles': persons_inner_circles,
                                    'HABIT_TYPE': game_relations.HABIT_TYPE,
                                    'place_meta_object': meta_relations.Place.create_from_object(context.place),
                                    'hero': heroes_logic.load_hero(account_id=context.account.id) if context.account else None,
                                    'places_power_storage': politic_power_storage.places,
                                    'persons_power_storage': politic_power_storage.persons,
                                    'job_power': job_power,
                                    'resource': context.resource})
