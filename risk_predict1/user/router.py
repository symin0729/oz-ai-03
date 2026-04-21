from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select

from auth.password import hash_password, verify_password
from database.connection import get_session
from user.request import SignUpRequest, LogInRequest
from user.models import User
from user.response import UserResponse

router = APIRouter(tags=["User"])

@router.post(
    "/users",
    summary="회원가입 API",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
)
async def signup_handler(
    body: SignUpRequest,
    session = Depends(get_session),
):
    # 1) 이메일 중복 검사
    stmt = select(User).where(User.email == body.email)
    result = await session.execute(stmt)
    user = result.scalar()

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 가입된 이메일입니다."
        )

    # 2) 비밀번호 해싱(암호화)
    password_hash = hash_password(plain_password=body.password)

    # 3) 회원 데이터 저장
    new_user = User(
        email=body.email,
        password_hash=password_hash,
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user) # id, created_at 새로고침
    
    return new_user


    # 1) 데이터 입력 (이메일, 비밀번호)
    # 2) 이메일 중복 검사 -> 이미 DB에 저장된 회원 데이터 중 해당 이메일로 가입한 사람이 이미 있는지 확인
    # 3) 비밀번호 해싱(암호화)
    # 4) 회원 데이터 저장
    # 5) 응답

@router.post(
    "/users/login",
    summary="로그인 API",
    status_code=status.HTTP_200_OK,
)
async def login_handler(
    body: LogInRequest,
    session = Depends(get_session),

):
    # 1) email로 사용자 조회 ()
    stmt = select(User).where(User.email == body.email)
    result = await session.execute(stmt)
    user = result.scalar

    # 사용자가 없는 경우
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="등록되지 않은 이메일입니다.",
        )

    # 3) 사용자가 있는 경우 :  요청 본문에서 온 body.password <vs> 사용자.password_hash 검증
    verified = verify_password(
        plain_password=body.password,
        password_hash=user.password_hash
    )
    # 비밀번호가 불일치 - error 발생
    if not verified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="비밀번호가 일치하지 않습니다."
        )

    # 4) JWT(JSON Web Token) 발급 - 임시 토큰 
    return

    # 1) 데이터 입력
    # 2) email로 사용자 조회 ()
    # 3) 요청 본문에서 온 body.password <vs> 사용자.password_hash 검증 
    # 4) JWT(JSON Web Token) 발급