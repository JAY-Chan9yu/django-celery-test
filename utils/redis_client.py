import redis


def get_redis_client() -> redis.Redis:
    redis_client = redis.Redis(
        host='127.0.0.1',
        db=5,
        port=63791,
        decode_responses=True,
        socket_timeout=3,
        socket_connect_timeout=1,
    )
    return redis_client

