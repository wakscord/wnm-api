from dependency_injector import containers, providers
from redis.asyncio import ConnectionPool, Redis

from app.common.settings import settings
from app.domain.proxy.repository import ProxyRedisRepository
from app.domain.proxy.service import ProxyService


class AppContainer(containers.DeclarativeContainer):
    redis_session = providers.Singleton(
        Redis,
        connection_pool=providers.Singleton(
            ConnectionPool, host=settings.REDIS_URL, port=6379, password=settings.REDIS_PASSWORD, decode_responses=True
        ),
    )
    proxy_repository = providers.Singleton(ProxyRedisRepository, session=redis_session)
    proxy_service = providers.Singleton(ProxyService, proxy_repo=proxy_repository)