from django.contrib.postgres.search import (
    SearchQuery, SearchRank, SearchVector, TrigramSimilarity,
)
from django.db import models


class NewSearchListView(models.Manager):
    """
    Display a News List page filtered by the search query.
    """
    #model = New
    #paginate_by = 10

    def search(self, text):
        query = SearchQuery(text, config='english')
        title_vector = SearchVector('title', weight='A', config='english')
        description_vector = SearchVector('description', weight='B', config='english')
        vectors = (title_vector + description_vector)
        search_rank = SearchRank(vectors, query)
        #trigram_similarity = TrigramSimilarity('title', text)
        return self.get_queryset().annotate(
            search = vectors
        ).filter(
            search = query
        ).annotate(
            rank = search_rank
        ).order_by('-rank')