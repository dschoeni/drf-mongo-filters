from rest_framework.filters import BaseFilterBackend
from drf_mongo_filters.filtersets import BaseFilterset, ModelFilterset
from qualname import qualname

class MongoFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filter_class = getattr(view,'filter_class', None)

        if filter_class is None:
            return queryset

        if not issubclass(filter_class, BaseFilterset):
            raise TypeError("%s expects filter_class to be %s: %s" % (qualname(self.__class__), qualname(BaseFilterset), repr(filter_class)))

        if not hasattr(view,'get_queryset'):
            raise TypeError("%s expects view to have get_queryset method" % (qualname(self.__class__),))

        if issubclass(filter_class, ModelFilterset):
            fs_model = filter_class.Meta.model
            qs_model = view.get_queryset()._document
            if not issubclass(qs_model, fs_model):
                raise TypeError("filter and view document class mismatch: %s vs %s " % (qualname(fs_model), qualname(qs_model)))

        filterset = filter_class(request.query_params)
        return filterset.filter_queryset(queryset)
