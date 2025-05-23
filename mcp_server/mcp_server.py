import os
from datetime import date, datetime, timedelta
from typing import List, Optional, Union, Any
from mcp.server.fastmcp import FastMCP
from otf_api import Otf, OtfUser, filters, models
from dotenv import load_dotenv

load_dotenv()

# Name your server appropriately
email = os.environ.get("OTF_EMAIL")
password = os.environ.get("OTF_PASSWORD")
otf = Otf(user=OtfUser(email, password))
mcp = FastMCP("OTF API MCP Server")

# from otf_api import functions to wrap around
@mcp.tool()
def get_today_date() -> str:
    """
    Returns today's date as an ISO string (YYYY-MM-DD).
    """
    return date.today().isoformat()

@mcp.tool()
def get_tomorrow_date() -> str:
    """
    Returns tomorrow's date as an ISO string (YYYY-MM-DD).
    """
    return (date.today() + timedelta(days=1)).isoformat()

@mcp.tool()
def get_date_offset(days: int) -> str:
    """
    Returns the date offset by a given number of days from today as an ISO string (YYYY-MM-DD).
    Positive for future, negative for past.
    """
    return (date.today() + timedelta(days=days)).isoformat()
# Booking & Class Management
@mcp.tool()
def get_bookings_new(start_date: Optional[Union[datetime, date, str]] = None, end_date: Optional[Union[datetime, date, str]] = None, exclude_cancelled: bool = True) -> List[models.BookingV2]:
    """
    Get the bookings for the user. If no dates are provided, it will return all bookings between today and 45 days from now.
    """
    return otf.get_bookings_new(start_date, end_date, exclude_cancelled)

@mcp.tool()
def get_booking_new(booking_id: str) -> models.BookingV2:
    """
    Get a specific booking by booking_id.
    """
    return otf.get_booking_new(booking_id)

@mcp.tool()
def get_classes(start_date: Optional[Union[date, str]] = None, end_date: Optional[Union[date, str]] = None, studio_uuids: Optional[List[str]] = None, include_home_studio: Optional[bool] = None, filters_: Optional[Union[List[filters.ClassFilter], filters.ClassFilter]] = None) -> List[models.OtfClass]:
    """
    Get classes for the given parameters.
    """
    return otf.get_classes(start_date, end_date, studio_uuids, include_home_studio, filters_)

@mcp.tool()
def get_booking(booking_uuid: str) -> models.Booking:
    """
    Get a booking by its UUID.
    """
    return otf.get_booking(booking_uuid)

@mcp.tool()
def get_booking_from_class(otf_class: Union[str, models.OtfClass]) -> models.Booking:
    """
    Get a booking from a class object or class UUID.
    """
    return otf.get_booking_from_class(otf_class)

@mcp.tool()
def get_booking_from_class_new(otf_class: Union[str, models.OtfClass, models.BookingV2Class]) -> models.BookingV2:
    """
    Get a new booking from a class object, class UUID, or BookingV2Class.
    """
    return otf.get_booking_from_class_new(otf_class)

@mcp.tool()
def book_class(otf_class: Union[str, models.OtfClass]) -> models.Booking:
    """
    Book a class by class UUID or OtfClass object.
    """
    return otf.book_class(otf_class)

@mcp.tool()
def book_class_new(class_id: str) -> models.BookingV2:
    """
    Book a class using the new booking system by class ID.
    """
    return otf.book_class_new(class_id)

@mcp.tool()
def cancel_booking(booking: Union[str, models.Booking]) -> None:
    """
    Cancel a booking by booking UUID or Booking object.
    """
    return otf.cancel_booking(booking)

@mcp.tool()
def cancel_booking_new(booking_id: str) -> None:
    """
    Cancel a booking using the new booking system by booking UUID.
    """
    return otf.cancel_booking_new(booking_id)

@mcp.tool()
def get_bookings(start_date: Optional[Union[date, str]] = None, end_date: Optional[Union[date, str]] = None, status: Optional[Union[models.BookingStatus, List[models.BookingStatus]]] = None, exclude_cancelled: bool = True, exclude_checkedin: bool = True) -> List[models.Booking]:
    """
    Get bookings with optional filters for date, status, and exclusion flags.
    """
    return otf.get_bookings(start_date, end_date, status, exclude_cancelled, exclude_checkedin)

@mcp.tool()
def get_historical_bookings() -> List[models.Booking]:
    """
    Get all historical bookings for the user.
    """
    return otf.get_historical_bookings()

# Studio Search & Management
@mcp.tool()
def get_studio_detail(studio_uuid: Optional[str] = None) -> models.StudioDetail:
    """
    Get details for a specific studio by UUID.
    """
    return otf.get_studio_detail(studio_uuid)

@mcp.tool()
def get_studios_by_geo(latitude: Optional[float] = None, longitude: Optional[float] = None) -> List[models.StudioDetail]:
    """
    Get studios by geographic coordinates.
    """
    return otf.get_studios_by_geo(latitude, longitude)

@mcp.tool()
def search_studios_by_geo(latitude: Optional[float] = None, longitude: Optional[float] = None, distance: int = 50) -> List[models.StudioDetail]:
    """
    Search for studios by geographic coordinates and distance.
    """
    return otf.search_studios_by_geo(latitude, longitude, distance)

@mcp.tool()
def get_favorite_studios() -> List[models.StudioDetail]:
    """
    Get the user's favorite studios.
    """
    return otf.get_favorite_studios()

@mcp.tool()
def add_favorite_studio(studio_uuids: Union[List[str], str]) -> List[models.StudioDetail]:
    """
    Add one or more studios to the user's favorites.
    """
    return otf.add_favorite_studio(studio_uuids)

@mcp.tool()
def remove_favorite_studio(studio_uuids: Union[List[str], str]) -> None:
    """
    Remove one or more studios from the user's favorites.
    """
    return otf.remove_favorite_studio(studio_uuids)

@mcp.tool()
def get_studio_services(studio_uuid: Optional[str] = None) -> List[models.StudioService]:
    """
    Get services offered by a specific studio.
    """
    return otf.get_studio_services(studio_uuid)

# Stats & Performance
@mcp.tool()
def get_member_lifetime_stats_in_studio(select_time: models.StatsTime = models.StatsTime.AllTime) -> models.InStudioStatsData:
    """
    Get the user's in-studio lifetime stats for a selected time period.
    """
    return otf.get_member_lifetime_stats_in_studio(select_time)

@mcp.tool()
def get_member_lifetime_stats_out_of_studio(select_time: models.StatsTime = models.StatsTime.AllTime) -> models.OutStudioStatsData:
    """
    Get the user's out-of-studio lifetime stats for a selected time period.
    """
    return otf.get_member_lifetime_stats_out_of_studio(select_time)

@mcp.tool()
def get_performance_summary(performance_summary_id: str) -> models.PerformanceSummary:
    """
    Get a performance summary by its ID.
    """
    return otf.get_performance_summary(performance_summary_id)

@mcp.tool()
def get_hr_history() -> List[models.TelemetryHistoryItem]:
    """
    Get the user's heart rate history.
    """
    return otf.get_hr_history()

@mcp.tool()
def get_telemetry(performance_summary_id: str, max_data_points: int = 150) -> models.Telemetry:
    """
    Get telemetry data for a performance summary.
    """
    return otf.get_telemetry(performance_summary_id, max_data_points)

@mcp.tool()
def get_body_composition_list() -> List[models.BodyCompositionData]:
    """
    Get the user's body composition data.
    """
    return otf.get_body_composition_list()

@mcp.tool()
def get_out_of_studio_workout_history() -> List[models.OutOfStudioWorkoutHistory]:
    """
    Get the user's out-of-studio workout history.
    """
    return otf.get_out_of_studio_workout_history()

# Challenge & Benchmarks
@mcp.tool()
def get_challenge_tracker() -> models.ChallengeTracker:
    """
    Get the user's challenge tracker data.
    """
    return otf.get_challenge_tracker()

@mcp.tool()
def get_benchmarks(challenge_category_id: int = 0, equipment_id: Union[models.EquipmentType, int] = 0, challenge_subcategory_id: int = 0) -> List[models.FitnessBenchmark]:
    """
    Get fitness benchmarks for the user.
    """
    return otf.get_benchmarks(challenge_category_id, equipment_id, challenge_subcategory_id)

@mcp.tool()
def get_benchmarks_by_equipment(equipment_id: models.EquipmentType) -> List[models.FitnessBenchmark]:
    """
    Get fitness benchmarks by equipment type.
    """
    return otf.get_benchmarks_by_equipment(equipment_id)

@mcp.tool()
def get_benchmarks_by_challenge_category(challenge_category_id: int) -> List[models.FitnessBenchmark]:
    """
    Get fitness benchmarks by challenge category.
    """
    return otf.get_benchmarks_by_challenge_category(challenge_category_id)

@mcp.tool()
def get_challenge_tracker_detail(challenge_category_id: int) -> models.FitnessBenchmark:
    """
    Get challenge tracker detail for a specific challenge category.
    """
    return otf.get_challenge_tracker_detail(challenge_category_id)

@mcp.tool()
def get_member_purchases() -> List[models.MemberPurchase]:
    """
    Get the user's purchase history.
    """
    return otf.get_member_purchases()

@mcp.tool()
def get_member_services(active_only: bool = True) -> Any:
    """
    Get the user's member services, optionally filtering for active only.
    """
    return otf.get_member_services(active_only)



@mcp.tool()
def get_favroite_studios_info() -> List[models.StudioDetail]:
    """
    Get favorite studios (optionally near a location).
    """
    return otf.get_favorite_studios()



mcp.run(transport="sse")