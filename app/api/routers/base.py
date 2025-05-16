from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.crud.base import check_connection
from api.dependencies import get_session_dev, get_session_prod

HEALTH_CHECK_ROUTE = "health-check"


router = APIRouter()


@router.get(f"/{HEALTH_CHECK_ROUTE}", response_model=dict)
async def check_health(session: Session = Depends(get_session_prod)):
    return check_connection(session)


router_dev = APIRouter()


@router_dev.get(f"/{HEALTH_CHECK_ROUTE}", response_model=dict)
async def check_health_dev(session: Session = Depends(get_session_dev)):
    return check_connection(session)
