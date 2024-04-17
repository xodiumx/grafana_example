from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.get("/2xx", response_model=None)
async def get_2xx() -> HTTPException:
    """Generate 2xx response"""
    raise HTTPException(
        detail='Ok',
        status_code=status.HTTP_200_OK
    )


@router.get("/4xx", response_model=None)
async def get_4xx() -> HTTPException:
    """Generate 4xx response"""
    raise HTTPException(
        detail='404 error',
        status_code=status.HTTP_404_NOT_FOUND
    )


@router.get("/5xx", response_model=None)
async def get_5xx() -> HTTPException:
    """Generate 5xx response"""
    raise HTTPException(
        detail='500 error',
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
