"""Main module."""
from dependency_injector.wiring import Provide, inject

from .listers import MovieLister

from .containers import Container


""" 
    the wire method and inject annotation supply the typed parameters to this function 
"""
@inject
def main(lister: MovieLister = Provide[Container.lister]) -> None:
    
    """ 
        example of getting movies by director and year
    """
    print("Francis Lawrence movies:")
    for movie in lister.movies_directed_by("Francis Lawrence"):
        print("\t-", movie)

    print("2016 movies:")
    for movie in lister.movies_released_in(2016):
        print("\t-", movie)


if __name__ == "__main__":
    container = Container()
    # inject the finder.type config parameter from the environment
    container.config.finder.type.from_env("MOVIE_FINDER_TYPE")
    container.wire(modules=[__name__])

    main()