from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.products import Product, ProductCreate, ProductUpdate

async def create_product(session: AsyncSession, product_create: ProductCreate) -> Product:
    db_product = Product(**product_create.model_dump())

    return db_product

async def update_product(session: AsyncSession, product: Product, product_update: ProductUpdate) -> Product:
    update_data = product_update.model_dump(exclude_unset=True)

    return product

async def get_product_by_id(session: AsyncSession, product_id: int) -> Product | None:
    result = await session.execute(
        select(Product).where(Product.id == product_id)
    )
    return result.scalar_one_or_none()