# SQlAlchemy를 이용해서 DB와 연결하는 코드
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# 데이터베이스 접속 정보 - 문자열 형태로 표시
# "sqlite://위치작성" -> 파일의 현재 경로로 만들어라
DATABASE_URL = "sqlite+aiosqlite:///./local.db"

# Engine : DB와 접속을 관리하는 객체, 자동차를 돌아가게 하는 게 엔진인데, sqlite를 돌아가게 만드는 것이 엔진.
async_engine = create_async_engine(DATABASE_URL, echo=True)
 
# Session: 한 번의 DB요청-응답 단위
AsyncSessionFactory = async_sessionmaker(
    bind=async_engine,
    # 데이터를 어떻게 다룰지를 조정하는 옵션
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)

# SQLAlchemy 세션을 관리하는 함수
async def get_async_session():
    session = AsyncSessionFactory()
    try:
        yield session
    finally:
        await session.close()