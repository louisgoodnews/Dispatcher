"""
Author: Louis Goodnews
Date: 2025-08-03
"""

import traceback
import uuid

from datetime import datetime
from enum import Enum
from typing import (
    Any,
    Callable,
    Dict,
    Final,
    Iterable,
    List,
    Optional,
    Self,
    Tuple,
    Union,
)

__all__: Final[List[str]] = [
    "DispatcherEvent",
    "DispatcherEventFactory",
    "DispatcherEventBuilder",
    "DispatcherEventNotification",
    "DispatcherEventNotificationFactory",
    "DispatcherEventNotificationBuilder",
    "DispatcherEventSubscription",
    "DispatcherEventSubscriptionBuilder",
    "DispatcherEventSubscriptionFactory",
    "Dispatcher",
]


class DispatcherEvent:
    """
    Represents an event in the Dispatcher system.
    This class encapsulates the details of an event, including its code, ID, name, and optional data.
    It provides methods to access these attributes and compare events for equality.

    Attributes:
        code (str): A unique code for the event.
        id (int): A unique identifier for the event.
        name (str): The name of the event.
        data (Dict[str, Any]): Optional dictionary containing additional data related to the event.
    """

    def __init__(
        self,
        code: str,
        id: int,
        name: str,
        data: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Initializes a new instance of the DispatcherEvent class.

        This constructor sets up the event with a unique code, ID, name, and optional data.

        :param code: The unique code for the event.
        :type code: str
        :param id: The unique identifier for the event.
        :type id: int
        :param name: The name of the event.
        :type name: str
        :param data: Optional dictionary containing additional data related to the event.
        :type data: Optional[Dict[str, Any]]

        :return: None
        :rtype: None
        """

        # Store the event code
        self._code: Final[str] = code

        # If data is None, initialize with an empty dictionary
        self._data: Dict[str, Any] = data if data is not None else {}

        # Store the event ID
        self._id: Final[int] = id

        # Initialize the last notified time to None
        # This attribute can be used to track when the event was last notified
        self._last_notified: Optional[datetime] = None

        # Store the name of the event
        self._name: Final[str] = name

    @property
    def code(self) -> str:
        """
        Returns the event code of the DispatcherEvent.

        This property provides access to the event code, which is a unique identifier for the event.


        :return: The event code.
        :rtype: str
        """

        # Return the event code
        # This code is typically a unique string that identifies the event
        # It is used to distinguish this event from others in the system
        # The code is set during the initialization of the event and remains constant throughout its lifetime
        # This property allows easy access to the event's code without needing to access the underlying
        # private attribute directly
        # It is useful for identifying the event in logs, user interfaces, or when comparing events
        # The code can be used in various ways, such as in database records, logs, or user interfaces
        # It is a fundamental part of the event's identity within the Dispatcher system
        # The code is immutable, meaning it cannot be changed after the event is created
        # This ensures that the event's identity remains consistent throughout its lifetime
        # The code is typically a string, but it can be any hashable type that serves as a unique identifier
        # In this case, it is a string, which is a common choice for unique identifiers
        # The code can be used to reference the event in other parts of the system, such as in subscriptions or handlers
        # It is important to ensure that the code is unique across all events in the system to avoid confusion
        # The code is typically assigned when the event is created, ensuring that it is unique
        # across all events in the system.
        # This uniqueness is crucial for tracking and managing events effectively.
        # The code is stored as a private attribute to encapsulate the event's data
        # and ensure that it is accessed in a controlled manner.
        # This encapsulation helps maintain the integrity of the event's code and ensures that
        # the code is accessed in a consistent way throughout the system.
        return self._code

    @property
    def data(self) -> Dict[str, Any]:
        """
        Returns the data associated with the DispatcherEvent.
        This property provides access to the data dictionary, which can contain additional information related to the event.

        :return: The data dictionary associated with the event.
        :rtype: Dict[str, Any]
        """

        # Return the data dictionary associated with the event
        # This dictionary can contain any additional information related to the event
        # It is useful for storing context or metadata about the event
        # The data is stored as a dictionary, allowing for flexible key-value pairs
        # The data can be accessed using the data property, which returns the entire dictionary
        # This allows for easy retrieval of all data associated with the event
        # The data can be modified by directly accessing the dictionary, allowing for dynamic updates
        # The data can be used to store any relevant information that is not part of the core
        # attributes of the event, such as user-defined metadata or additional context
        # It is important to ensure that the data dictionary is used consistently across the system
        # to avoid confusion or errors when accessing or modifying the data
        # The data dictionary can be empty if no additional information is provided
        # during the event creation, allowing for flexibility in event definitions
        # The data can be used in various ways, such as logging, debugging, or passing
        # additional context to event handlers or subscribers
        # It is a key part of the event's structure, allowing for extensibility and customization
        # The data property provides a convenient way to access the event's data without needing
        # to access the underlying private attribute directly
        # This encapsulation helps maintain the integrity of the event's data and ensures that
        # the data is accessed in a controlled manner
        return self._data

    @property
    def id(self) -> int:
        """
        Returns the unique identifier of the DispatcherEvent.
        This property provides access to the event ID, which is a unique integer that identifies the event.

        :return: The unique identifier of the event.
        :rtype: int
        """

        # Return the unique identifier of the event
        # This ID is typically used to track the event in logs or for debugging purposes
        # It is a unique integer that distinguishes this event from others in the system
        # The ID is set during the initialization of the event and remains constant throughout its lifetime
        # This property allows easy access to the event's ID without needing to access the underlying
        # private attribute directly
        # It is useful for identifying the event in logs, user interfaces, or when comparing events
        # The ID can be used to reference the event in other parts of the system, such as in subscriptions or handlers
        # It is important to ensure that the ID is unique across all events in the system to avoid confusion
        # The ID is typically an integer, but it can be any hashable type that serves as a unique identifier
        # In this case, it is an integer, which is a common choice for unique identifiers
        # The ID can be used in various ways, such as in database records, logs, or user interfaces
        # It is a fundamental part of the event's identity within the Dispatcher system
        # The ID is immutable, meaning it cannot be changed after the event is created
        # This ensures that the event's identity remains consistent throughout its lifetime
        # The ID is typically assigned when the event is created, ensuring that it is unique
        # across all events in the system. This uniqueness is crucial for tracking and
        # managing events effectively.
        return self._id

    @property
    def last_notified(self) -> Optional[datetime]:
        """
        Returns the last notified time of the DispatcherEvent.
        This property provides access to the last time the event was notified, which can be useful for tracking event notifications.

        :return: The last notified time of the event, or None if it has not been notified yet.
        :rtype: Optional[datetime]
        """

        # Return the last notified time of the event
        # This is useful for tracking when the event was last processed or notified
        # It can be used to implement throttling or rate limiting for event notifications
        return self._last_notified

    @last_notified.setter
    def last_notified(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the last notified time of the DispatcherEvent.
        This setter allows updating the last notified time, which can be useful for tracking event notifications.

        :param value: The new last notified time to set, or None if it has not been notified yet.
        :type value: datetime

        :return: None
        :rtype: None
        """

        # Set the last notified time of the event
        # This is useful for tracking when the event was last processed or notified
        # It can be used to implement throttling or rate limiting for event notifications
        self._last_notified = value

    @property
    def name(self) -> str:
        """
        Returns the name of the DispatcherEvent.
        This property provides access to the name of the event, which is a human-readable identifier.

        :return: The name of the event.
        :rtype: str
        """

        # Return the name of the event
        # This is useful for identifying the event in logs or user interfaces
        # The name is a string that describes the event, making it easier to understand its purpose
        # It is typically used for display purposes, such as in logs or user interfaces
        # The name can be used to categorize or identify the event in a more human-readable way
        # It is not intended to be a unique identifier, but rather a descriptive label for the event
        # This property allows easy access to the event's name without needing to access the underlying
        # private attribute directly
        return self._name

    def __contains__(
        self,
        key: str,
    ) -> bool:
        """
        Checks if the DispatcherEvent contains a specific key in its data dictionary.
        This method allows checking for the presence of a key in the event's data.

        :param key: The key to check for in the data dictionary.
        :type key: str

        :return: True if the key exists in the data dictionary, False otherwise.
        :rtype: bool
        """

        # Check if the key exists in the data dictionary
        # This allows for quick lookups to see if the event has specific data associated with it
        # It is useful for checking if certain information is available in the event's data
        return key in self.data

    def __eq__(
        self,
        value: object,
    ) -> bool:
        """
        Compares this DispatcherEvent with another object for equality.
        Two events are considered equal if their codes, IDs, and names match.

        :param value: The object to compare against.
        :type value: object

        :return: True if the events are equal, False otherwise.
        :rtype: bool
        """

        # Check if the value is an instance of DispatcherEvent
        if not isinstance(
            value,
            DispatcherEvent,
        ):
            # If not, return False
            return False

        # Compare the code, ID, and name of both events
        return self.code == value.code and self.id == value.id and self.name == value.name

    def __getitem__(
        self,
        key: str,
    ) -> Any:
        """
        Retrieves the value associated with the given key from the event's data dictionary.
        This method allows access to the data stored in the event using a key.

        :param key: The key to look up in the data dictionary.
        :type key: str

        :return: The value associated with the key in the data dictionary.
        :rtype: Any

        :raises KeyError: If the key does not exist in the data dictionary.
        """

        # Check if the key exists in the data dictionary
        if key not in self.data:
            # If not, raise a KeyError
            raise KeyError(f"Key '{key}' not found in event data.")

        # Return the value associated with the key
        return self.data[key]

    def __repr__(self) -> str:
        """
        Returns a string representation of the DispatcherEvent.

        This method provides a human-readable representation of the event, including its code, ID, name, and data.

        :return: A string representation of the event.
        :rtype: str
        """

        # Format the string representation of the DispatcherEvent
        # Include the class name, code, ID, name, and data
        # This is useful for debugging and logging purposes
        # It provides a clear overview of the event's attributes
        # The __class__.__name__ is used to get the name of the class dynamically
        return (
            f"{self.__class__.__name__}(code={self.code}, id={self.id}, name={self.name}, "
            f"data={self.data})"
        )

    def __setitem__(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Sets the value for the given key in the event's data dictionary.
        This method allows modification of the data stored in the event.

        :param key: The key to set in the data dictionary.
        :type key: str
        :param value: The value to associate with the key.
        :type value: Any

        :return: None
        :rtype: None
        """

        # Set the value for the given key in the data dictionary
        self.data[key] = value

    def __str__(self) -> str:
        """
        Returns a string representation of the DispatcherEvent.

        This method provides a human-readable representation of the event, including its code, ID, name, and data.

        :return: A string representation of the event.
        :rtype: str
        """

        # Call the __repr__ method to get the string representation
        # This ensures that the string representation is consistent with the __repr__ method
        # This is useful for debugging and logging purposes
        # It provides a clear overview of the event's attributes
        # The __repr__ method is designed to return a detailed representation of the object
        # This method is typically used for debugging and logging
        # It provides a more detailed view of the object's state compared to __str__
        # The __str__ method is designed to return a user-friendly string representation of the object
        # This method is typically used for displaying the object in a user interface or console
        # In this case, we are using __repr__ to ensure that the string representation is
        # consistent and detailed, which is useful for debugging and logging purposes
        return self.__repr__()

    def clear(self) -> None:
        """
        Clears the data dictionary of the DispatcherEvent.
        This method removes all key-value pairs from the event's data dictionary.

        :return: None
        :rtype: None
        """

        # Clear the data dictionary
        # This removes all key-value pairs from the event's data
        # It effectively resets the data to an empty state
        self.data.clear()

    def compare_to(
        self,
        other: "DispatcherEvent",
    ) -> bool:
        """
        Compares this DispatcherEvent with another DispatcherEvent for equality.
        Two events are considered equal if their codes, IDs, and names match.

        :param other: The other DispatcherEvent to compare against.
        :type other: DispatcherEvent

        :return: True if the events are equal, False otherwise.
        :rtype: bool
        """

        # Compare the code, ID, and name of both events
        return self == other

    def is_empty(self) -> bool:
        """
        Checks if the DispatcherEvent has no data.

        This method returns True if the event's data dictionary is empty, indicating that
        there is no additional information associated with the event.

        :return: True if the event has no data, False otherwise.
        :rtype: bool
        """

        # Check if the data dictionary is empty
        return not self.data


class DispatcherEventFactory:
    """
    Factory class for creating DispatcherEvent instances.
    This class provides methods to create events with unique IDs and codes.

    Methods:
        create_dispatcher_event(name: str, data: Optional[Dict[str, Any]] = None) -> DispatcherEvent:
            Creates a new DispatcherEvent with a unique ID and code.
    """

    # Unique base ID for generating event IDs.
    # This base ID is used to ensure that event IDs are unique across the system.
    # It is set to a high value to avoid collisions with other IDs in the system.
    _base_id: int = 10000

    @classmethod
    def create_dispatcher_event(
        cls,
        name: str,
        data: Optional[Dict[str, Any]] = None,
    ) -> DispatcherEvent:
        """
        Creates a new DispatcherEvent with a unique ID and code.

        :param name: The name of the event.
        :type name: str
        :param data: Optional dictionary containing additional data related to the event.
        :type data: Optional[Dict[str, Any]]

        :return: A new instance of DispatcherEvent.
        :rtype: DispatcherEvent
        """

        # Generate a unique code for the event using uuid4
        # This ensures that each event has a unique identifier
        # The uuid4 function generates a random UUID, which is suitable for use as a unique
        # identifier in distributed systems
        # The code is converted to a string to match the expected type for the event code
        code: str = str(uuid.uuid4())

        # Create and return a new DispatcherEvent instance
        result: DispatcherEvent = DispatcherEvent(
            code=code,
            data=data,
            id=cls._base_id,
            name=name,
        )

        # Increment the base ID for the next event
        cls._base_id += 1

        # Return the newly created event
        return result


class DispatcherEventBuilder:
    """
    Builder class for constructing DispatcherEvent instances.
    This class allows for flexible configuration of event attributes before finalizing it into a DispatcherEvent instance.
    It provides methods to set various attributes of the event, such as data, name, and other configuration options.

    Methods:
        build() -> DispatcherEvent:
            Builds and returns a DispatcherEvent based on the current configuration.
        with_data(**kwargs: Dict[str, Any]) -> Self:
            Sets the data for the event being built using keyword arguments.
        with_name(value: str) -> Self:
            Sets the name of the event being built.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the DispatcherEventBuilder class.
        This constructor sets up the builder with an empty configuration dictionary,
        which will be used to build a DispatcherEvent.
        The configuration dictionary allows for flexible configuration of the event's attributes
        before finalizing it into a DispatcherEvent instance.

        This builder pattern allows for a more readable and maintainable way to create
        DispatcherEvent instances by chaining method calls to set various attributes.

        :return: None
        :rtype: None
        """

        # Initialize the builder with an empty configuration dictionary.
        # This dictionary will hold the configuration for the event being built.
        # It allows for flexible configuration of the event's attributes before finalizing it.
        self._configuration: Dict[str, Any] = {}

    def build(self) -> DispatcherEvent:
        """
        Builds and returns a DispatcherEvent based on the current configuration.

        :return: A new instance of DispatcherEvent with the configured attributes.
        :rtype: DispatcherEvent

        :raises ValueError: If the required attributes (code, id, name) are not set in the configuration.
        """

        # Check if the required attributes are present in the configuration.
        if not "name" in self._configuration:
            # If any required attribute is missing, raise a ValueError.
            raise ValueError("Missing required attributes to build DispatcherEvent.")

        # Create and return a new DispatcherEvent instance with the current configuration.
        return DispatcherEventFactory.create_dispatcher_event(
            data=self._configuration.get(
                "data",
                {},
            ),
            name=self._configuration["name"],
        )

    def with_data(
        self,
        **kwargs: Any,
    ) -> Self:
        """
        Sets the data for the event being built using keyword arguments.

        :param kwargs: Key-value pairs representing the data for the event.

        :return: The current instance of DispatcherEventBuilder for method chaining.
        :rtype: Self
        """

        # Check, if 'data' is not already in the configuration dictionary.
        if "data" not in self._configuration:
            # If not, initialize it with an empty dictionary.
            self._configuration["data"] = {}

        # Update the configuration dictionary with the provided keyword arguments.
        self._configuration["data"].update(**kwargs)

        # Return the current instance to allow for method chaining.
        return self

    def with_name(
        self,
        value: str,
    ) -> Self:
        """
        Sets the name of the event being built.

        :param value: The name to set for the event.
        :type value: str

        :return: The current instance of DispatcherEventBuilder for method chaining.
        :rtype: Self
        """

        # Set the 'name' key in the configuration dictionary to the provided value.
        self._configuration["name"] = value

        # Return the current instance to allow for method chaining.
        return self


class DispatcherEventNotificationStatus(Enum):
    """
    Enum representing the status of a DispatcherEventNotification.
    This enum defines the possible statuses that a notification can have in the Dispatcher system.
    """

    # Status indicating that the notification was successful.
    SUCCESS = "success"

    # Status indicating that the notification failed.
    FAILURE = "failure"


class DispatcherEventNotification:
    """
    Represents a notification in the Dispatcher system.
    This class encapsulates the details of a notification, including its content, duration, end time, errors,
    associated event, namespace, and start time.

    Attributes:
        content (Dict[str, Any]): The content of the notification.
        duration (float): The duration of the notification in seconds.
        end (datetime): The end time of the notification.
        errors (List[Dict[str, Any]]): A list of errors associated with the notification.
        event (DispatcherEvent): The associated DispatcherEvent for this notification.
        id (int): The unique identifier for the notification.
        namespace (str): The namespace associated with the notification.
        start (datetime): The start time of the notification.
        status (DispatcherEventNotificationStatus): The status of the notification, indicating whether it was successful or failed.
    """

    def __init__(
        self,
        content: Dict[str, Any],
        end: datetime,
        errors: List[Dict[str, Any]],
        event: DispatcherEvent,
        id: int,
        namespace: str,
        start: datetime,
        status: DispatcherEventNotificationStatus,
    ) -> None:
        """
        Initializes a new instance of the DispatcherEventNotification class.
        This constructor sets up the notification with its content, end time, errors, associated event, namespace, and start time.

        :param content: The content of the notification.
        :type content: Dict[str, Any]
        :param end: The end time of the notification.
        :type end: datetime
        :param errors: A list of errors associated with the notification.
        :type errors: List[Dict[str, Any]]
        :param event: The associated DispatcherEvent for this notification.
        :type event: DispatcherEvent
        :param id: The unique identifier for the notification.
        :type id: int
        :param namespace: The namespace associated with the notification.
        :type namespace: str
        :param start: The start time of the notification.
        :type start: datetime
        :param status: The status of the notification, indicating whether it was successful or failed.
        :type status: DispatcherEventNotificationStatus

        :return: None
        :rtype: None
        """

        # Store the content of the notification.
        self._content: Final[Dict[str, Any]] = content

        # Store the duration of the notification as the difference between end and start times.
        self._duration: Final[float] = (end - start).total_seconds()

        # Store the content of the notification.
        self._end: Final[datetime] = end

        # Store the errors associated with the notification.
        self._errors: Final[List[Dict[str, Any]]] = errors

        # Store the associated DispatcherEvent for this notification.
        self._event: Final[DispatcherEvent] = event

        # Store the unique identifier for the notification.
        self._id: Final[int] = id

        # Store the namespace associated with the notification.
        self._namespace: Final[str] = namespace

        # Store the start time of the notification.
        self._start: Final[datetime] = start

        # Store the status of the notification.
        self._status: Final[DispatcherEventNotificationStatus] = status

    @property
    def content(self) -> Dict[str, Any]:
        """
        Returns the content of the notification.

        This property provides access to the content dictionary associated with the notification.

        :return: The content of the notification.
        :rtype: Dict[str, Any]
        """

        # Return the content of the notification
        return self._content

    @property
    def duration(self) -> float:
        """
        Returns the duration of the notification in seconds.

        This property calculates the duration as the difference between the end and start times.

        :return: The duration of the notification in seconds.
        :rtype: float
        """

        # Return the duration of the notification
        return self._duration

    @property
    def end(self) -> datetime:
        """
        Returns the end time of the notification.

        This property provides access to the end time of the notification.

        :return: The end time of the notification.
        :rtype: datetime
        """

        # Return the end time of the notification
        return self._end

    @property
    def errors(self) -> List[Dict[str, Any]]:
        """
        Returns the list of errors associated with the notification.

        This property provides access to the errors that occurred during the notification process.

        :return: The list of errors associated with the notification.
        :rtype: List[Dict[str, Any]]
        """

        # Return the list of errors associated with the notification
        return self._errors

    @property
    def event(self) -> DispatcherEvent:
        """
        Returns the associated DispatcherEvent for this notification.

        This property provides access to the event that triggered the notification.

        :return: The associated DispatcherEvent.
        :rtype: DispatcherEvent
        """

        # Return the associated DispatcherEvent for this notification
        return self._event

    @property
    def id(self) -> int:
        """
        Returns the unique identifier of the notification.

        This property provides access to the unique ID assigned to the notification.

        :return: The unique identifier of the notification.
        :rtype: int
        """

        # Return the unique identifier of the notification
        return self._id

    @property
    def namespace(self) -> str:
        """
        Returns the namespace associated with the notification.

        This property provides access to the namespace under which the notification was created.

        :return: The namespace associated with the notification.
        :rtype: str
        """

        # Return the namespace associated with the notification
        return self._namespace

    @property
    def start(self) -> datetime:
        """
        Returns the start time of the notification.

        This property provides access to the start time of the notification.

        :return: The start time of the notification.
        :rtype: datetime
        """

        # Return the start time of the notification
        return self._start

    @property
    def status(self) -> DispatcherEventNotificationStatus:
        """
        Returns the status of the notification.

        This property provides access to the status of the notification, indicating whether it was successful or failed.

        :return: The status of the notification.
        :rtype: DispatcherEventNotificationStatus
        """

        # Return the status of the notification
        return self._status

    def __contains__(
        self,
        key: str,
    ) -> bool:
        """
        Checks if the notification contains a specific key in its content dictionary.

        This method allows checking for the presence of a key in the notification's content.

        :param key: The key to check for in the content dictionary.
        :type key: str

        :return: True if the key exists in the content dictionary, False otherwise.
        :rtype: bool
        """

        # Check if the key exists in the content dictionary
        return key in self.content

    def __getitem__(
        self,
        key: str,
    ) -> Any:
        """
        Retrieves the value associated with the given key from the notification's content.

        This method allows access to the content stored in the notification using a key.

        :param key: The key to look up in the content dictionary.
        :type key: str

        :return: The value associated with the key in the content dictionary.
        :rtype: Any

        :raises KeyError: If the key does not exist in the content dictionary.
        """

        # Check if the key exists in the content dictionary
        if key not in self.content:
            # If not, raise a KeyError
            raise KeyError(f"Key '{key}' not found in notification content.")

        # Return the value associated with the key
        return self.content[key]

    def __repr__(self) -> str:
        """
        Returns a string representation of the DispatcherEventNotification.
        This method provides a human-readable representation of the notification, including its content, duration, end time, errors, associated event, id, namespace, and start time.

        :return: A string representation of the notification.
        :rtype: str
        """

        # Format the string representation of the DispatcherEventNotification
        # Include the class name, content, end time, errors, associated event, namespace, and start time
        # This is useful for debugging and logging purposes
        return (
            f"{self.__class__.__name__}(content={self.content}, duration={self.duration}, end={self.end}, "
            f"errors={self.errors}, event={self.event}, id={self.id}, namespace={self.namespace}, "
            f"start={self.start})"
        )

    def __setitem__(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Sets the value for the given key in the notification's content.

        This method allows modification of the content stored in the notification.

        :param key: The key to set in the content dictionary.
        :type key: str
        :param value: The value to associate with the key.
        :type value: Any

        :return: None
        :rtype: None

        :raises ValueError: Due to the content attribute being immutable.
        """

        raise ValueError(
            f"The 'content' attribute of this {self.__class__.__name__} class object is immutable. Use the constructor to set content."
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the DispatcherEventNotification.
        This method provides a human-readable representation of the notification, including its content, end time, errors, associated event, namespace, and start time.

        :return: A string representation of the notification.
        :rtype: str
        """

        # Call the __repr__ method to get the string representation
        # This ensures that the string representation is consistent with the __repr__ method
        return self.__repr__()

    def get_function_names(self) -> List[str]:
        """
        Returns the function names of the notification's content dictionary.

        :return: The function names of the notification's content dictionary.
        :rtype: List[str]
        """

        # Return the contents of the notification
        return list(self.content.keys())

    def get_function_results(self) -> List[Any]:
        """
        Returns the function results of the notification's content dictionary.

        :return: The function results of the notification's content dictionary.
        :rtype: List[Any]
        """

        # Return the contents of the notification
        return list(self.content.values())

    def get_one_and_only_result(self) -> Optional[Any]:
        """
        Returns the one and only result from the notification's content dictionary.
        If the content dictionary is empty or has more than one key-value pair, it returns None.
        If the content dictionary has exactly one key-value pair, it returns the value of that single
        key.

        :return: The value of the single key in the content dictionary if it exists, otherwise None.
        :rtype: Optional[Any]
        """

        # Check if the content dictionary is empty
        if not self.content:
            # If the content dictionary is empty, return None
            return None

        # Check if the content dictionary has exactly one key-value pair
        if len(self.content) == 1:
            # If it does, return the value of that single key
            return next(iter(self.content.values()))

        # If the content dictionary has more than one key-value pair, raise a ValueError
        # This indicates that the notification does not have a single result
        raise ValueError(
            f"Notification content has more than one result: {self.content}. Expected exactly one result."
        )

    def handle(self) -> bool:
        """
        Handles the notification.

        This method is called when the notification is received.

        Returns:
            bool: True if the notification was handled successfully, False otherwise.

        Raises:
            ValueError: If the notification has more than one result.
        """

        # Check if the notification has errors
        if self.has_errors():
            # If the notification has errors, raise a ValueError
            raise ValueError(
                f"Notification has errors: {self.errors}. Expected no errors.",
            )

        # Return True
        return True

    def has_errors(self) -> bool:
        """
        Checks if the notification has any associated errors.

        This method returns True if there are errors in the notification, otherwise False.

        :return: True if there are errors, False otherwise.
        :rtype: bool
        """

        # Check if the errors list is not empty
        return len(self.errors) > 0


class DispatcherEventNotificationFactory:
    """
    Factory class for creating DispatcherEventNotification instances.
    This class provides methods to create notifications with unique IDs and associated events.

    Methods:
        create_dispatcher_notification(
            end: datetime,
            event: DispatcherEvent,
            namespace: str,
            start: datetime,
            status: DispatcherEventNotificationStatus,
            content: Optional[Dict[str, Any]] = None,
            errors: Optional[List[Dict[str, Any]]] = None,
        ) -> DispatcherEventNotification:
            Creates a new DispatcherEventNotification with the specified parameters.
    """

    # Unique base ID for generating notification IDs.
    # This base ID is used to ensure that notification IDs are unique across the system.
    # It is set to a high value to avoid collisions with other IDs in the system.
    _base_id: int = 10000

    @classmethod
    def create_dispatcher_notification(
        cls,
        end: datetime,
        event: DispatcherEvent,
        namespace: str,
        start: datetime,
        status: DispatcherEventNotificationStatus,
        content: Optional[Dict[str, Any]] = None,
        errors: Optional[List[Dict[str, Any]]] = None,
    ) -> DispatcherEventNotification:
        """
        Creates a new DispatcherEventNotification with the specified parameters.

        :param end: The end time of the notification.
        :type end: datetime
        :param event: The associated DispatcherEvent for this notification.
        :type event: DispatcherEvent
        :param namespace: The namespace associated with the notification.
        :type namespace: str
        :param start: The start time of the notification.
        :type start: datetime
        :param status: The status of the notification, indicating whether it was successful or failed.
        :type status: DispatcherEventNotificationStatus
        :param content: Optional dictionary containing the content of the notification.
        :type content: Optional[Dict[str, Any]]
        :param errors: Optional list of errors associated with the notification.
        :type errors: Optional[List[Dict[str, Any]]]

        :return: A new instance of DispatcherEventNotification.
        :rtype: DispatcherEventNotification
        """

        # Create a new DispatcherEventNotification instance with the provided parameters.
        # This method initializes a notification with its content, end time, errors, associated event,
        # namespace, and start time.
        result: DispatcherEventNotification = DispatcherEventNotification(
            content=content or {},
            end=end,
            errors=errors or [],
            event=event,
            id=cls._base_id,
            namespace=namespace,
            start=start,
            status=status,
        )

        # Increment the base ID for the next notification
        cls._base_id += 1

        # Return the newly created notification
        return result


class DispatcherEventNotificationBuilder:
    """
    Builder class for constructing DispatcherEventNotification instances.
    This class allows for flexible configuration of notification attributes before finalizing it into a DispatcherEventNotification instance.
    It provides methods to set various attributes of the notification, such as content, end time, errors, associated event, namespace, and start time.

    Methods:
        with_content(**kwargs: Dict[str, Any]) -> Self:
            Sets the content for the notification being built using keyword arguments.
        with_end(value: datetime) -> Self:
            Sets the end time for the notification being built.
        with_errors(*args: Iterable[Dict[str, Any]]) -> Self:
            Sets the errors for the notification being built using a list of dictionaries.
        with_event(value: DispatcherEvent) -> Self:
            Sets the associated DispatcherEvent for the notification being built.
        with_namespace(value: str) -> Self:
            Sets the namespace for the notification being built.
        with_start(value: datetime) -> Self:
            Sets the start time for the notification being built.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the DispatcherEventNotificationBuilder class.
        This constructor sets up the builder with an empty configuration dictionary,
        which will be used to build a DispatcherEventNotification.
        The configuration dictionary allows for flexible configuration of the notification's attributes
        before finalizing it into a DispatcherEventNotification instance.

        This builder pattern allows for a more readable and maintainable way to create
        DispatcherEventNotification instances by chaining method calls to set various attributes.

        :return: None
        :rtype: None"""

        # Initialize the builder with an empty configuration dictionary.
        # This dictionary will hold the configuration for the notification being built.
        # It allows for flexible configuration of the notification's attributes before finalizing it.
        # The configuration dictionary is structured to hold the necessary attributes for the notification,
        # such as content, end time, errors, associated event, namespace, and start time
        # The dictionary is initialized as empty, and attributes can be added dynamically.
        # The keys of the dictionary are the attribute names, and the values are the corresponding values
        # This structure allows for efficient management of notification attributes, enabling
        # a flexible and extensible way to build notifications.
        self._configuration: Dict[str, Any] = {}

    def build(self) -> DispatcherEventNotification:
        """
        Builds and returns a DispatcherEventNotification based on the current configuration.

        :return: A new instance of DispatcherEventNotification with the configured attributes.
        :rtype: DispatcherEventNotification

        :raises ValueError: If the required attributes (end, event, namespace, start) are not set in the configuration.
        """

        # Check if the required attributes are present in the configuration.
        if not all(
            key in self._configuration
            for key in (
                "end",
                "event",
                "namespace",
                "start",
            )
        ):
            # If any required attribute is missing, raise a ValueError.
            raise ValueError("Missing required attributes to build DispatcherEventNotification.")

        # Create and return a new DispatcherEventNotification instance with the current configuration.
        return DispatcherEventNotificationFactory.create_dispatcher_notification(
            content=self._configuration.get(
                "content",
                {},
            ),
            end=self._configuration["end"],
            event=self._configuration["event"],
            namespace=self._configuration["namespace"],
            start=self._configuration["start"],
            status=self._configuration.get(
                "status",
                DispatcherEventNotificationStatus.SUCCESS,
            ),
            errors=self._configuration.get(
                "errors",
                [],
            ),
        )

    def with_content(
        self,
        **kwargs: Any,
    ) -> Self:
        """
        Sets the content for the notification being built using keyword arguments.

        :param kwargs: Key-value pairs representing the content for the notification.

        :return: The current instance of DispatcherEventNotificationBuilder for method chaining.
        :rtype: Self
        """

        # Check, if 'content' is not already in the configuration dictionary.
        if "content" not in self._configuration:
            # If not, initialize it with an empty dictionary.
            self._configuration["content"] = {}

        # Update the configuration dictionary with the provided keyword arguments.
        self._configuration["content"].update(**kwargs)

        # Return the current instance to allow for method chaining.
        return self

    def with_end(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the end time for the notification being built.

        :param value: The end time to set for the notification.
        :type value: datetime

        :return: The current instance of DispatcherEventNotificationBuilder for method chaining.
        :rtype: Self
        """

        # Set the 'end' key in the configuration dictionary to the provided value.
        self._configuration["end"] = value

        # Return the current instance to allow for method chaining.
        return self

    def with_errors(
        self,
        *args: Any,
    ) -> Self:
        """
        Sets the errors for the notification being built using a list of dictionaries.

        :param args: A variable number of dictionaries representing errors for the notification.

        :return: The current instance of DispatcherEventNotificationBuilder for method chaining.
        :rtype: Self
        """

        # Check, if 'errors' is not already in the configuration dictionary.
        if "errors" not in self._configuration:
            # If not, initialize it with an empty list.
            self._configuration["errors"] = []

        # Extend the 'errors' list with the provided arguments.
        self._configuration["errors"].extend(*args)

        # Return the current instance to allow for method chaining.
        return self

    def with_event(
        self,
        value: DispatcherEvent,
    ) -> Self:
        """
        Sets the associated DispatcherEvent for the notification being built.

        :param value: The DispatcherEvent to associate with the notification.
        :type value: DispatcherEvent

        :return: The current instance of DispatcherEventNotificationBuilder for method chaining.
        :rtype: Self
        """

        # Set the 'event' key in the configuration dictionary to the provided value.
        self._configuration["event"] = value

        # Return the current instance to allow for method chaining.
        return self

    def with_namespace(
        self,
        value: str,
    ) -> Self:
        """
        Sets the namespace for the notification being built.

        :param value: The namespace to set for the notification.
        :type value: str

        :return: The current instance of DispatcherEventNotificationBuilder for method chaining.
        :rtype: Self
        """

        # Set the 'namespace' key in the configuration dictionary to the provided value.
        self._configuration["namespace"] = value

        # Return the current instance to allow for method chaining.
        return self

    def with_start(
        self,
        value: datetime,
    ) -> Self:
        """
        Sets the start time for the notification being built.

        :param value: The start time to set for the notification.
        :type value: datetime

        :return: The current instance of DispatcherEventNotificationBuilder for method chaining.
        :rtype: Self
        """

        # Set the 'start' key in the configuration dictionary to the provided value.
        self._configuration["start"] = value

        # Return the current instance to allow for method chaining.
        return self

    def with_status(
        self,
        value: DispatcherEventNotificationStatus,
    ) -> Self:
        """
        Sets the status for the notification being built.

        :param value: The status to set for the notification.
        :type value: DispatcherEventNotificationStatus

        :return: The current instance of DispatcherEventNotificationBuilder for method chaining.
        :rtype: Self
        """

        # Set the 'status' key in the configuration dictionary to the provided value.
        self._configuration["status"] = value

        # Return the current instance to allow for method chaining.
        return self


class DispatcherEventSubscription:
    """
    Represents a subscription to events in the Dispatcher system.
    This class manages event subscriptions, associating functions with namespaces and handling their persistence.
    It uses a normalized data structure to efficiently store and retrieve subscription information.

    Attributes:
        _id (Final[int]): A unique identifier for this subscription object.
        _function_id_to_function (Final[Dict[str, Dict[str, Union[bool, Callable[[Any], Any]]]]]):
            A dictionary mapping a unique function ID (UUID) to a dictionary containing the
            callable function and a boolean indicating if it's persistent.
        _namespace_to_function_id (Final[Dict[str, List[str]]]):
            A dictionary mapping a namespace to a list of function IDs that are subscribed to it.
    """

    def __init__(
        self,
        id: int,
        **kwargs: Any,
    ) -> None:
        """
        Initializes a new instance of the DispatcherEventSubscription class.

        This constructor sets up the data structures for managing event subscriptions.
        It can also initialize subscriptions from keyword arguments, making it compatible
        with the factory and builder classes.

        :param id: The unique identifier for this subscription instance.
        :param kwargs: Optional keyword arguments to initialize subscriptions. The key is the namespace,
                       and the value is a list of subscription tuples (function, persistent, function_id).
        """

        self._function_id_to_function: Final[
            Dict[str, Dict[str, Union[bool, Callable[[Any], Any]]]]
        ] = {}
        self._id: Final[int] = id
        self._namespace_to_function_id: Final[Dict[str, List[str]]] = {}

        if kwargs:
            for namespace, subscriptions in kwargs.items():
                if namespace not in self._namespace_to_function_id:
                    self._namespace_to_function_id[namespace] = []

                for subscription_tuple in subscriptions:
                    function, persistent, function_id = subscription_tuple

                    self._namespace_to_function_id[namespace].append(function_id)
                    self._function_id_to_function[function_id] = {
                        "function": function,
                        "persistent": persistent,
                    }

    @property
    def id(self) -> int:
        """
        Returns the unique identifier of the subscription.

        This property provides access to the unique ID assigned to the subscription,
        which is used to identify the subscription within the Dispatcher system.

        :return: The unique identifier of the subscription.
        :rtype: int
        """

        # Return the unique identifier of the subscription
        return self._id

    def __getitem__(
        self,
        key: str,
    ) -> List[Tuple[Callable[[Any], Any], bool, str]]:
        """
        Retrieves the list of subscriptions for a given namespace using dictionary-style access.

        :param key: The namespace to look up.
        :return: A list of tuples for each subscription, or an empty list if the namespace is not found.
                 Each tuple contains (function, is_persistent, function_id).
        """
        return self.get_subscribers_for_namespace(key)

    def __repr__(self) -> str:
        """
        Returns a concise string representation of the DispatcherEventSubscription instance.

        :return: A string representation of the object.
        """
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"namespaces={list(self._namespace_to_function_id.keys())}, "
            f"subscriptions={len(self._function_id_to_function)})"
        )

    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the DispatcherEventSubscription instance.

        :return: A string representation of the object.
        """
        return self.__repr__()

    def contains(
        self,
        function_id: Optional[str] = None,
        namespace: Optional[str] = None,
    ) -> bool:
        """
        Checks if a subscription exists by function ID or if a namespace has any subscriptions.

        :param function_id: The unique ID of the function to check for.
        :param namespace: The namespace to check for.
        :return: True if the subscription or namespace exists, False otherwise.
        :raises AttributeError: If neither function_id nor namespace is provided.
        """

        # If a function ID is provided, check if it exists in the function ID to function mapping.
        if function_id:
            # Check if the function ID exists in the function ID to function mapping.
            return function_id in self._function_id_to_function

        # If a namespace is provided, check if it exists in the namespace to function ID mapping.
        elif namespace:
            # Check if the namespace exists in the namespace to function ID mapping.
            return namespace in self._namespace_to_function_id

        # If neither function_id nor namespace is provided, raise an AttributeError.
        else:
            # At least one of 'function_id' or 'namespace' must be provided.
            raise AttributeError("At least one of 'function_id' or 'namespace' must be provided.")

    def clear(self) -> None:
        """
        Clears all subscriptions, removing all namespaces and functions.
        """

        # Clear the function ID to function mapping.
        self._function_id_to_function.clear()

        # Clear the namespace to function ID mapping.
        self._namespace_to_function_id.clear()

    def dispatch(
        self,
        event: DispatcherEvent,
        builder: DispatcherEventNotificationBuilder,
        namespace: str,
        *args: Iterable[Any],
        **kwargs: Dict[str, Any],
    ) -> DispatcherEventNotificationBuilder:
        """
        Dispatches an event to all functions subscribed to the given namespace.

        It executes each subscribed function and updates the notification builder with the results.
        Non-persistent subscriptions are removed after execution.

        :param event: The event to dispatch.
        :param builder: The notification builder to update with results.
        :param namespace: The namespace to dispatch the event to.
        :param args: Positional arguments to pass to the subscribed functions.
        :param kwargs: Keyword arguments to pass to the subscribed functions.

        :return: The updated notification builder.
        :raises KeyError: If the namespace does not exist.
        """

        # Check if the namespace exists.
        if namespace not in self._namespace_to_function_id:
            # If the namespace does not exist, return the builder as is.
            return builder

        # Copy the list of function IDs to avoid modification issues during iteration.
        function_ids_to_dispatch: List[str] = self._namespace_to_function_id[namespace][:]

        # List to store non-persistent function IDs.
        non_persistent_ids: List[str] = []

        # List of tuples containing function ID and subscription details, sorted by priority.
        function_id_to_subscription_details: List[
            Tuple[str, Dict[str, Union[bool, Callable[[Any], Any]]]]
        ] = sorted(
            [
                (function_id, self._function_id_to_function.get(function_id))
                for function_id in function_ids_to_dispatch
            ],
            key=lambda x: x[1]["priority"],
        )

        for (
            function_id,
            subscription_details,
        ) in function_id_to_subscription_details:
            if not subscription_details:
                # This can happen if a function was unsubscribed concurrently.
                continue

            # Get the function from the subscription details.
            function: Callable[[Any], Any] = subscription_details["function"]

            # Check if the subscription is persistent.
            is_persistent: bool = subscription_details["persistent"]

            # Check if the subscription is non-persistent.
            if not is_persistent:
                # Add the function ID to the list of non-persistent IDs.
                non_persistent_ids.append(function_id)

            try:
                # Execute the function.
                result: Any = function(event, *args, **kwargs)

                # Add the result to the notification builder.
                builder.with_content(**{function.__name__: result})

                # Set the status to success.
                builder.with_status(value=DispatcherEventNotificationStatus.SUCCESS)
            except Exception as e:
                # Add the error to the notification builder.
                builder.with_errors(
                    [
                        {
                            "function_id": function_id,
                            "error": str(e),
                            "function": function.__name__,
                            "namespace": namespace,
                            "traceback": traceback.format_exc(),
                        }
                    ]
                )

                # Set the status to failure.
                builder.with_status(value=DispatcherEventNotificationStatus.FAILURE)

        # Clean up non-persistent subscriptions.
        for function_id in non_persistent_ids:
            try:
                # Unsubscribe the function from the namespace.
                self.unsubscribe_by_function_id(function_id)
            except KeyError:
                # Might have already been removed by another operation, which is fine.
                pass

        # Update the last notified time of the event.
        event.last_notified = datetime.now()

        # Return the updated notification builder.
        return builder

    def get_status(
        self,
        function_id: str,
    ) -> Optional[Tuple[Callable[[Any], Any], bool, str]]:
        """
        Retrieves the status of a subscription by its unique ID.

        :param function_id: The unique ID of the subscription to look up.
        :return: A tuple containing (function, is_persistent, function_id) if found, otherwise None.
        """

        # Check if the function ID exists in the function ID to function mapping.
        if function_id in self._function_id_to_function:

            # Get the subscription details.
            details: Dict[str, Union[bool, Callable[[Any], Any]]] = self._function_id_to_function[
                function_id
            ]

            # Return the function, persistence setting, and function ID.
            return (details["function"], details["persistent"], function_id)

        # If the function ID is not found, return None.
        return None

    def get_subscribers_for_namespace(
        self,
        namespace: str,
    ) -> List[Tuple[Callable[[Any], Any], bool, str]]:
        """
        Retrieves the list of subscribers for a given namespace.

        This method returns all subscriptions associated with the specified namespace in a format
        that is compatible with other parts of the system.

        :param namespace: The namespace to retrieve subscribers for.
        :return: A list of tuples, where each tuple is (function, is_persistent, function_id).
                 Returns an empty list if the namespace has no subscribers.
        """

        # Check if the namespace exists in the namespace to function ID mapping.
        if namespace not in self._namespace_to_function_id:
            # If the namespace does not exist, return an empty list.
            return []

        subscribers: List[Tuple[Callable[[Any], Any], bool, str]] = []

        # Iterate over the function IDs associated with the namespace.
        for function_id in self._namespace_to_function_id[namespace]:

            # Check if the function ID exists in the function ID to function mapping.
            if function_id in self._function_id_to_function:

                # Get the subscription details.
                details: Dict[str, Union[bool, Callable[[Any], Any]]] = (
                    self._function_id_to_function[function_id]
                )

                # Append the function, persistence setting, and function ID to the list.
                subscribers.append(
                    (
                        details["function"],
                        details["persistent"],
                        function_id,
                    )
                )

        # Return the list of subscribers.
        return subscribers

    def subscribe(
        self,
        namespace: str,
        function: Callable[[Any], Any],
        persistent: bool = False,
        priority: int = 0,
    ) -> str:
        """
        Subscribes a function to a namespace.

        This method associates a function with a namespace, allowing it to receive events
        dispatched to that namespace. It generates a unique ID for the subscription.

        :param namespace: The namespace to subscribe the function to.
        :type namespace: str
        :param function: The function to be subscribed.
        :type function: Callable[[Any], Any]
        :param persistent: If True, the subscription will not be automatically removed after being triggered once.
                           Defaults to False.
        :type persistent: bool
        :param priority: The priority of the subscription.
        :type priority: int

        :return: A unique function ID for the subscription.
        :rtype: str

        :raises ValueError: If the function is already subscribed to the given namespace.
        """

        # Ensure the namespace exists in the tracking dictionary.
        if namespace not in self._namespace_to_function_id:
            # If the namespace does not exist, create it.
            self._namespace_to_function_id[namespace] = []
        else:
            # Check if the same function is already subscribed to this namespace.
            for function_id in self._namespace_to_function_id[namespace]:
                # Check if the function is already subscribed to this namespace.
                if self._function_id_to_function[function_id]["function"] == function:
                    # If the function is already subscribed, raise a ValueError.
                    raise ValueError(
                        f"Function '{function.__name__}' is already subscribed to namespace '{namespace}'."
                    )

        # Generate a unique ID for this specific subscription.
        function_id = str(uuid.uuid4())

        # Link the function ID to the namespace.
        self._namespace_to_function_id[namespace].append(function_id)

        # Store the function and its persistence setting using the unique ID.
        self._function_id_to_function[function_id] = {
            "function": function,
            "persistent": persistent,
            "priority": priority,
        }

        # Return the unique ID so the subscription can be managed later.
        return function_id

    def unsubscribe(
        self,
        function_id: Optional[str] = None,
        namespace: Optional[str] = None,
        function: Optional[Callable[[Any], Any]] = None,
    ) -> bool:
        """
        Unsubscribes a function based on its ID, namespace, or the function object.

        This method provides multiple ways to remove a subscription. Only one parameter should be provided.

        :param function_id: The unique ID of the subscription to remove.
        :param namespace: The namespace from which to remove all subscriptions.
        :param function: The function object to unsubscribe from all namespaces.
        :return: True if the unsubscription was successful.
        :raises ValueError: If no identifying parameter is provided, or if the subscription is not found.
        """

        # Check if a function ID is provided.
        if function_id is not None:
            # Unsubscribe the function using its unique subscription ID.
            return self.unsubscribe_by_function_id(function_id)

        # Check if a namespace is provided.
        elif namespace is not None:
            # Unsubscribe all functions from the specified namespace.
            return self.unsubscribe_by_namespace(namespace)

        # Check if a function object is provided.
        elif function is not None:
            # Unsubscribe the function from all namespaces it is subscribed to.
            return self.unsubscribe_by_function(function)

        # If no identifying parameter is provided, raise a ValueError.
        else:
            # At least one of 'function_id', 'namespace', or 'function' must be provided.
            raise ValueError(
                "At least one parameter (function_id, namespace, or function) must be provided."
            )

    def unsubscribe_all(self) -> None:
        """
        Removes all subscriptions from all namespaces.
        """

        # Clear all functions.
        self._function_id_to_function.clear()

        # Clear all namespaces.
        self._namespace_to_function_id.clear()

    def unsubscribe_by_function_id(self, function_id: str) -> bool:
        """
        Unsubscribes a function using its unique subscription ID.

        :param function_id: The unique ID of the subscription to remove.
        :return: True if the unsubscription was successful.
        :raises KeyError: If the function ID is not found.
        """

        # Check if the function ID is in the registry.
        if function_id not in self._function_id_to_function:
            # If the function ID is not found, raise a KeyError.
            raise KeyError(f"Function ID '{function_id}' not found.")

        # Remove the function from the central registry.
        self._function_id_to_function.pop(function_id, None)

        # Remove the function ID from any namespace that contains it.
        found: bool = False

        # Iterate over all namespaces.
        for namespace, id_list in self._namespace_to_function_id.items():
            # Check if the function ID is in the namespace.
            if function_id not in id_list:
                # If the function ID is not found, continue to the next namespace.
                continue

            # Remove the function ID from the namespace.
            id_list.remove(function_id)

            # Clean up empty namespace.
            if not id_list:
                # Remove the namespace from the registry.
                self._namespace_to_function_id.pop(namespace)

            # Set the found flag to True.
            found = True

            # Break out of the loop since a function ID should be unique across all namespaces.
            break

        # Return the found flag.
        return found

    def unsubscribe_by_function(
        self,
        function: Callable[[Any], Any],
    ) -> bool:
        """
        Unsubscribes a specific function from all namespaces it is subscribed to.

        :param function: The function object to unsubscribe.
        :type function: Callable[[Any], Any]

        :return: True if at least one subscription was removed.
        :rtype: bool

        :raises ValueError: If the function is not subscribed to any namespace.
        """

        # Find all function IDs associated with this function object.
        function_ids_to_remove: List[str] = [
            fid
            for fid, data in self._function_id_to_function.items()
            if data["function"] == function
        ]

        # Check if the function is subscribed to any namespace.
        if not function_ids_to_remove:
            # If the function is not subscribed to any namespace, raise a ValueError.
            raise ValueError(f"Function '{function.__name__}' not found in any subscription.")

        # Unsubscribe each found instance.
        for function_id in function_ids_to_remove:
            # Unsubscribe the function using its unique subscription ID.
            self.unsubscribe_by_function_id(function_id)

        # Return True.
        return True

    def unsubscribe_by_function(
        self,
        function: Callable[[Any], Any],
    ) -> bool:
        """
        Unsubscribes a specific function from all namespaces it is subscribed to.

        :param function: The function object to unsubscribe.
        :return: True if at least one subscription was removed.
        :raises ValueError: If the function is not subscribed to any namespace.
        """

        # Find all function IDs associated with this function object.
        function_ids_to_remove: List[str] = [
            fid
            for fid, data in self._function_id_to_function.items()
            if data["function"] == function
        ]

        # Check if the function is subscribed to any namespace.
        if not function_ids_to_remove:
            # If the function is not subscribed to any namespace, raise a ValueError.
            raise ValueError(f"Function '{function.__name__}' not found in any subscription.")

        # Unsubscribe each found instance.
        for function_id in function_ids_to_remove:
            # Unsubscribe the function using its unique subscription ID.
            self.unsubscribe_by_function_id(function_id)

        # Return True.
        return True

    def unsubscribe_by_namespace(
        self,
        namespace: str,
    ) -> bool:
        """
        Unsubscribes all functions from a specific namespace.

        :param namespace: The namespace to clear of all subscriptions.
        :return: True if the namespace was found and cleared.
        :raises KeyError: If the namespace does not exist.
        """

        # Check if the namespace exists.
        if namespace not in self._namespace_to_function_id:
            # If the namespace does not exist, raise a KeyError.
            raise KeyError(f"Namespace '{namespace}' not found.")

        # Get all function IDs for the namespace.
        function_ids_to_remove: List[str] = self._namespace_to_function_id.pop(namespace)

        # Remove each function from the central registry.
        for function_id in function_ids_to_remove:
            # Remove the function from the central registry.
            self._function_id_to_function.pop(
                function_id,
                None,
            )

        # Return True.
        return True


class DispatcherEventSubscriptionFactory:
    """
    Factory class for creating DispatcherEventSubscription instances.
    This class provides methods to create event subscriptions with unique identifiers and manage them.

    Methods:
        create_dispatcher_event_subscription() -> DispatcherEventSubscription:
            Creates a new DispatcherEventSubscription instance.
    """

    # Unique base ID for generating subscription IDs.
    # This base ID is used to ensure that subscription IDs are unique across the system.
    # It is set to a high value to avoid collisions with other IDs in the system.
    _base_id: int = 10000

    @classmethod
    def create_dispatcher_event_subscription(
        cls,
        **kwargs: Dict[str, List[Tuple[Callable[[Any], Any], bool, str]]],
    ) -> DispatcherEventSubscription:
        """
        Creates a new DispatcherEventSubscription instance.

        :param kwargs: Optional keyword arguments to initialize the subscription data.
        :type kwargs: Dict[str, Optional[List[Tuple[Callable[[Any], Any], bool, str]]]]

        :return: A new instance of DispatcherEventSubscription.
        :rtype: DispatcherEventSubscription
        """

        # Create a new instance of DispatcherEventSubscription
        result: DispatcherEventSubscription = DispatcherEventSubscription(
            id=cls._base_id,
            **kwargs,
        )

        # Increment the base ID for the next subscription
        cls._base_id += 1

        # Return the newly created subscription
        return result


class DispatcherEventSubscriptionBuilder:
    """
    Builder class for constructing DispatcherEventSubscription instances.
    This class allows for flexible configuration of subscription attributes before finalizing it into a DispatcherEventSubscription instance.
    It provides methods to set various attributes of the subscription, such as id, data, and functions.

    Methods:
        with_data(**kwargs: Dict[str, List[Tuple[Callable[[Any], Any], bool, str]]]) -> Self:
            Sets the data for the subscription being built using keyword arguments.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the DispatcherEventSubscriptionBuilder class.
        This constructor sets up the builder with an empty configuration dictionary,
        which will be used to build a DispatcherEventSubscription.
        The configuration dictionary allows for flexible configuration of the subscription's attributes
        before finalizing it into a DispatcherEventSubscription instance.

        :return: None
        :rtype: None
        """

        # Initialize the builder with an empty configuration dictionary.
        # This dictionary will hold the configuration for the subscription being built.
        # It allows for flexible configuration of the subscription's attributes before finalizing it.
        self._configuration: Dict[str, Any] = {}

    def with_data(
        self,
        **kwargs: Dict[str, List[Tuple[Callable[[Any], Any], bool, str]]],
    ) -> Self:
        """
        Sets the data for the subscription being built using keyword arguments.

        :param kwargs: Key-value pairs representing the data for the subscription.
        :type kwargs: Dict[str, List[Tuple[Callable[[Any], Any], bool, str]]]

        :return: The current instance of DispatcherEventSubscriptionBuilder for method chaining.
        :rtype: Self
        """

        # Update the configuration dictionary with the provided keyword arguments.
        self._configuration.update(kwargs)

        # Return the current instance to allow for method chaining.
        return self

    def build(self) -> DispatcherEventSubscription:
        """
        Builds and returns a new DispatcherEventSubscription instance with the configured attributes.

        :return: A new instance of DispatcherEventSubscription.
        :rtype: DispatcherEventSubscription
        """

        # Create a new DispatcherEventSubscription instance with the current configuration.
        # This method initializes a subscription with its data, which includes functions, persistence flags,
        # and unique codes for each subscription.
        return DispatcherEventSubscriptionFactory.create_dispatcher_event_subscription(
            **self._configuration
        )
        # The configuration dictionary is passed to the factory method, which creates a new subscription
        # with the specified attributes. The factory method ensures that the subscription is created
        # with a unique ID and initializes it with the provided data.


class Dispatcher:
    """
    Dispatcher class for managing event subscriptions and dispatching events.
    This class allows for subscribing functions to specific events, dispatching those events,
    and managing the subscriptions efficiently.

    Attributes:
        _subscriptions (Dict[str, DispatcherEventSubscription]):
            A dictionary mapping event names to their corresponding DispatcherEventSubscription instances.
            Each subscription manages the functions that are subscribed to specific events.

    Methods:
        __init__() -> None:
            Initializes a new instance of the Dispatcher class with an empty dictionary for subscriptions.
        subscriptions() -> Dict[str, DispatcherEventSubscription]:
            Returns the current subscriptions of the dispatcher.
        __getitem__(key: str) -> Optional[DispatcherEventSubscription]:
            Retrieves the subscription for a given event name.
        bulk_dispatch(events: Iterable[DispatcherEvent], namespace: str, *args: Iterable[Any], **kwargs: Dict[str, Any]) -> List[DispatcherEventNotification]:
            Dispatches multiple events to the subscribed functions in the specified namespace.
        bulk_subscribe(events: Iterable[DispatcherEvent], namespace: str, function: Callable[[Any], Any], persistent: bool = False) -> List[str]:
            Subscribes multiple functions to a namespace with an optional persistence flag.
        bulk_unsubscribe(events: Iterable[DispatcherEvent], namespace: str, function: Optional[Callable[[Any], Any]] = None) -> List[bool]:
            Unsubscribes multiple functions from a namespace or by their unique codes.
        dispatch(event: DispatcherEvent, namespace: str, *args: Iterable[Any], **kwargs: Dict[str, Any]) -> DispatcherEventNotification:
            Dispatches an event to the subscribed functions in the specified namespace.
        subscribe(namespace: str, function: Callable[[Any], Any], persistent: bool = False) -> str:
            Subscribes a function to a namespace with an optional persistence flag.
        unsubscribe(code: Optional[str] = None, namespace: Optional[str] = None, function: Optional[Callable[[Any], Any]] = None) -> Optional[bool]:
            Unsubscribes a function from a namespace or by its unique code.
        unsubscribe_all() -> None:
            Unsubscribes all functions from all namespaces, effectively clearing all subscriptions.
        unsubscribe_by_code(code: str) -> Optional[bool]:
            Unsubscribes a function from a namespace using its unique code.
        unsubscribe_by_event(event: DispatcherEvent) -> Optional[bool]:
            Unsubscribes a function from a namespace using the event's name.
        unsubscribe_by_function(function: Callable[[Any], Any]) -> Optional[bool]:
            Unsubscribes a function from all namespaces.
        unsubscribe_by_namespace(namespace: str) -> Optional[bool]:
            Unsubscribes all functions from a specific namespace.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Dispatcher class.
        This constructor sets up the dispatcher with an empty dictionary to hold event subscriptions.

        The dictionary will map event names to their corresponding DispatcherEventSubscription instances.
        Each subscription will manage the functions that are subscribed to specific events.

        :return: None
        :rtype: None
        """

        # Initialize the dispatcher with an empty dictionary to hold event subscriptions.
        # This dictionary will map event names to their corresponding DispatcherEventSubscription instances.
        # Each subscription will manage the functions that are subscribed to specific events.
        # The dictionary is structured as follows:
        # {
        #     "event_name1": DispatcherEventSubscription(...),
        #     "event_name2": DispatcherEventSubscription(...),
        # }
        self._subscriptions: Final[Dict[str, DispatcherEventSubscription]] = {}

    @property
    def subscriptions(self) -> Dict[str, DispatcherEventSubscription]:
        """
        Returns the current subscriptions of the dispatcher.

        This property provides access to the dictionary of event subscriptions managed by the dispatcher.
        Each key in the dictionary is an event name, and each value is a DispatcherEventSubscription instance
        that manages the functions subscribed to that event.

        :return: The dictionary of event subscriptions.
        :rtype: Dict[str, DispatcherEventSubscription]
        """

        # Return the current subscriptions of the dispatcher
        return self._subscriptions

    def __getitem__(
        self,
        key: str,
    ) -> Optional[DispatcherEventSubscription]:
        """
        Retrieves the subscription for a given event name.

        This method allows accessing the subscription associated with a specific event name.
        If the event name does not exist in the subscriptions, it returns None.

        :param key: The event name for which to retrieve the subscription.
        :type key: str

        :return: The DispatcherEventSubscription associated with the event name, or None if not found.
        :rtype: Optional[DispatcherEventSubscription]
        """

        # Return the subscription for the given event name, or None if it does not exist
        return self._subscriptions.get(
            key,
            None,
        )

    def bulk_dispatch(
        self,
        events: Iterable[DispatcherEvent],
        namespace: str,
        *args: Iterable[Any],
        **kwargs: Dict[str, Any],
    ) -> List[DispatcherEventNotification]:
        """
        Dispatches multiple events to the subscribed functions in the specified namespace.
        This method iterates over a list of DispatcherEvent instances and dispatches each one,
        returning a list of DispatcherEventNotification instances for each dispatched event.

        :param events: An iterable of DispatcherEvent instances to be dispatched.
        :type events: Iterable[DispatcherEvent]
        :param namespace: The namespace to which the events belong.
        :type namespace: str
        :param args: Additional positional arguments to pass to the subscribed functions.
        :type args: Iterable[Any]
        :param kwargs: Additional keyword arguments to pass to the subscribed functions.
        :type kwargs: Dict[str, Any]

        :return: A list of DispatcherEventNotification instances for each dispatched event.
        :rtype: List[DispatcherEventNotification]
        """

        # Initialize an empty list to hold the notifications for each dispatched event
        notifications: List[DispatcherEventNotification] = []

        # Iterate over each event in the provided iterable of events
        for event in events:
            # Dispatch the current event and append the resulting notification to the list
            notifications.append(
                self.dispatch(
                    event=event,
                    namespace=namespace,
                    *args,
                    **kwargs,
                )
            )

        # Return the list of notifications for all dispatched events
        return notifications

    def dispatch(
        self,
        event: DispatcherEvent,
        namespace: str,
        *args: Iterable[Any],
        **kwargs: Dict[str, Any],
    ) -> DispatcherEventNotification:
        """
        Dispatches an event to the subscribed functions in the specified namespace.
        This method creates a DispatcherEventNotification for the event and notifies all functions
        subscribed to the event in the given namespace.

        :param event: The DispatcherEvent to be dispatched.
        :type event: DispatcherEvent
        :param namespace: The namespace to which the event belongs.
        :type namespace: str
        :param args: Additional positional arguments to pass to the subscribed functions.
        :type args: Iterable[Any]
        :param kwargs: Additional keyword arguments to pass to the subscribed functions.
        :type kwargs: Dict[str, Any]

        :return: A DispatcherEventNotification containing the event data and notification details.
        :rtype: DispatcherEventNotification
        """

        # Create a new DispatcherEventNotificationBuilder instance to build the notification
        # This builder will be used to construct a notification that will be sent to the subscribed functions
        # The builder allows for flexible configuration of the notification's attributes
        # before finalizing it into a DispatcherEventNotification instance.
        result: DispatcherEventNotificationBuilder = DispatcherEventNotificationBuilder()

        # Set the start time for the notification being built
        # This marks the beginning of the notification's lifecycle, allowing for tracking of its duration
        # The start time is set to the current datetime, indicating when the notification was created.
        result.with_start(value=datetime.now())

        # Set the content for the notification being built
        # The content is set to the data associated with the event being dispatched.
        # This allows the notification to carry the relevant information about the event
        # that is being dispatched, such as its metadata, name, and any other relevant details
        result.with_event(value=event)

        # Set the namespace for the event being dispatched
        result.with_namespace(value=namespace)

        # Check if the event's name exists in the subscriptions
        # This allows the dispatcher to notify all subscribed functions for the given event
        # If the namespace does not exist, it will not dispatch the event, and the notification
        # will not be sent to any functions.
        # This is useful for ensuring that events are only dispatched to namespaces that have
        # active subscriptions, preventing unnecessary processing and improving performance.
        # The namespace is used to identify the group of functions that should be notified
        # when the event occurs. It acts as a filter for the subscriptions, allowing the dispatcher
        # to efficiently route events to the appropriate functions based on their namespace.
        # If the namespace exists, the dispatcher will proceed to dispatch the event to the functions
        # subscribed to that namespace, allowing them to process the event and perform any necessary actions.
        # If the namespace does not exist, the dispatcher will not dispatch the event,
        # and the notification will not be sent to any functions.
        # This ensures that only relevant functions are notified, reducing overhead and improving efficiency.
        if self._subscriptions.get(
            event.name,
            None,
        ):
            # If the event's name exists in the subscriptions, dispatch the event to it
            # This allows the dispatcher to notify all subscribed functions for the given event
            self._subscriptions[event.name].dispatch(
                event=event,
                builder=result,
                namespace=namespace,
                *args,
                **kwargs,
            )

        # If the namespace does not exist, the dispatcher will not dispatch the event,
        # and the notification will not be sent to any functions.
        # This ensures that only relevant functions are notified, reducing overhead and improving efficiency.
        result.with_end(value=datetime.now())

        # Build and return the DispatcherEventNotification instance with the configured attributes
        # The notification will contain the event data, namespace, start and end times,
        # and any errors that occurred during the dispatch process.
        # This allows the notification to be sent to the subscribed functions,
        # providing them with the necessary information to process the event.
        return result.build()

    def get_subscribers_for_namespace(
        self,
        namespace: str,
    ) -> List[Tuple[Callable[[Any], Any], bool, str]]:
        """
        Retrieves the subscribers for a specific namespace.
        This method returns a list of tuples containing the functions, their persistence status,
        and unique codes for each subscription in the specified namespace.

        :param namespace: The namespace for which to retrieve the subscribers.
        :type namespace: str

        :return: A list of tuples containing the function, persistence flag, and code for each subscriber,
                 or None if the namespace does not exist.
        :rtype: Optional[List[Tuple[Callable[[Any], Any], bool, str]]]
        """

        # Initialize an empty list to hold the results of subscribers for the given namespace
        results: Optional[List[Tuple[Callable[[Any], Any], bool, str]]] = []

        # Iterate through the subscriptions in the data dictionary
        # The data dictionary contains namespaces as keys and lists of subscriptions as values
        for subscription in self._subscriptions.values():
            # Check if the subscription has a namespace that matches the provided namespace
            results.extend(subscription.get_subscribers_for_namespace(namespace=namespace))

        # Return the list of subscribers for the given namespace.
        # If the namespace does not exist in the subscription data, return None.
        return results

    def bulk_subscribe(
        self,
        events: Iterable[Union[DispatcherEvent, str]],
        function: Callable[[Any], Any],
        namespace: str,
        persistent: bool = False,
        priority: int = 0,
    ) -> List[str]:
        """
        Subscribes a function to multiple events in the specified namespace.
        This method allows a function to be associated with multiple events, enabling it to receive notifications
        when any of the events are dispatched.

        :param events: An iterable of DispatcherEvent or event names (as strings) to subscribe to.
        :type events: Iterable[Union[DispatcherEvent, str]]
        :param function: The function to be subscribed to the events.
        :type function: Callable[[Any], Any]
        :param namespace: The namespace to which the events belong.
        :type namespace: str
        :param persistent: Whether the subscription should persist across restarts.
        :type persistent: bool
        :param priority: The priority of the subscription.
        :type priority: int

        :return: A list of unique codes representing the subscriptions.
        :rtype: List[str]
        """

        # Initialize an empty list to hold the unique codes for each subscription
        codes: List[str] = []

        # Iterate over each event in the provided iterable of events
        for event in events:
            # Subscribe the function to the event and append the resulting code to the list
            codes.append(
                self.subscribe(
                    event=event,
                    function=function,
                    namespace=namespace,
                    persistent=persistent,
                    priority=priority,
                )
            )

        # Return the list of unique codes for all subscriptions
        return codes

    def subscribe(
        self,
        event: Union[DispatcherEvent, str],
        function: Callable[[Any], Any],
        namespace: str,
        persistent: bool = False,
        priority: int = 0,
    ) -> str:
        """
        Subscribes a function to an event in the specified namespace.
        This method allows a function to be associated with an event, enabling it to receive notifications
        when the event is dispatched.

        :param event: The DispatcherEvent to subscribe to.
        :type event: DispatcherEvent
        :param function: The function to be subscribed to the event.
        :type function: Callable[[Any], Any]
        :param namespace: The namespace to which the event belongs.
        :type namespace: str
        :param persistent: Whether the subscription should persist across restarts.
        :type persistent: bool
        :param priority: The priority of the subscription.
        :type priority: int

        :return: A unique code representing the subscription.
        :rtype: str
        """

        # Check if the event is an instance of string
        if isinstance(
            event,
            str,
        ):
            # If the event is a string, create a DispatcherEvent with the name set to the string value
            # This allows for subscribing to events that are identified by their names as strings.
            # The DispatcherEvent is initialized with the name and an empty data dictionary.
            event = DispatcherEventFactory.create_dispatcher_event(name=event)

        # Check if the event's name exists in the subscriptions
        if event.name not in self._subscriptions:
            # If not, create a new DispatcherEventSubscription for the event's name
            # This initializes a new subscription for the event, allowing functions to be subscribed to it.
            # The subscription will manage the functions that are subscribed to the event,
            # including their persistence status and unique codes.
            # The subscription is created using the DispatcherEventSubscriptionFactory,
            # which ensures that the subscription is initialized with a unique ID and an empty data structure.
            # The factory method creates a new instance of DispatcherEventSubscription,
            # which will hold the functions, persistence flags, and unique codes for the subscriptions.
            # This allows the dispatcher to manage subscriptions efficiently and ensures that each event
            # has its own dedicated subscription instance.
            self._subscriptions[event.name] = (
                DispatcherEventSubscriptionFactory.create_dispatcher_event_subscription()
            )

        # Subscribe the event to the event's name and return the unique code for the subscription
        return self._subscriptions[event.name].subscribe(
            namespace=namespace,
            function=function,
            persistent=persistent,
            priority=priority,
        )

    def bulk_unsubscribe(
        self,
        function_ids: Iterable[str] = (),
        events: Iterable[DispatcherEvent] = (),
        functions: Iterable[Callable[[Any], Any]] = (),
        namespaces: Iterable[str] = (),
    ) -> List[bool]:
        """
        Unsubscribes multiple functions from events based on the provided parameters.

        :param function_ids: An iterable of unique function IDs for the subscriptions to be removed.
        :param events: An iterable of DispatcherEvent instances to unsubscribe from.
        :param functions: An iterable of functions to be unsubscribed.
        :param namespaces: An iterable of namespaces from which to unsubscribe all functions.
        :return: A list of booleans indicating the success of each unsubscription.
        """
        results: List[bool] = []

        for function_id in function_ids:
            results.append(self.unsubscribe_by_function_id(function_id=function_id))

        for event in events:
            results.append(self.unsubscribe_by_event(event=event))

        for function in functions:
            results.append(self.unsubscribe_by_function(function=function))

        for namespace in namespaces:
            results.append(self.unsubscribe_by_namespace(namespace=namespace))

        return results

    def unsubscribe(
        self,
        function_id: Optional[str] = None,
        event: Optional[DispatcherEvent] = None,
        function: Optional[Callable[[Any], Any]] = None,
        namespace: Optional[str] = None,
    ) -> bool:
        """
        Unsubscribes a function from an event based on the provided parameters.

        :param function_id: The unique ID of the subscription to remove.
        :param event: The event to unsubscribe from.
        :param function: The function to unsubscribe.
        :param namespace: The namespace to unsubscribe from.
        :return: True if the unsubscription was successful.
        :raises ValueError: If no identifying parameter is provided.
        """
        if function_id is not None:
            return self.unsubscribe_by_function_id(function_id=function_id)
        elif event is not None:
            return self.unsubscribe_by_event(event=event)
        elif function is not None:
            return self.unsubscribe_by_function(function=function)
        elif namespace is not None:
            return self.unsubscribe_by_namespace(namespace=namespace)
        else:
            raise ValueError(
                "At least one parameter (function_id, event, function, or namespace) must be provided."
            )

    def unsubscribe_all(self) -> None:
        """
        Unsubscribes all functions from all events, clearing all subscriptions.
        """
        self._subscriptions.clear()

    def unsubscribe_by_function_id(self, function_id: str) -> bool:
        """
        Unsubscribes a function from an event using its unique function ID.

        :param function_id: The unique ID of the subscription to remove.
        :return: True if the subscription was successfully removed.
        :raises KeyError: If no subscription with the given function ID is found.
        """
        for subscription in self._subscriptions.values():
            try:
                # This will succeed if the function_id is in this subscription object.
                if subscription.unsubscribe_by_function_id(function_id=function_id):
                    return True
            except (KeyError, ValueError):
                continue

        raise KeyError(f"No subscription found with function ID '{function_id}'.")

    def unsubscribe_by_event(
        self,
        event: DispatcherEvent,
    ) -> Optional[bool]:
        """
        Unsubscribes a function from an event using the event's name.
        This method removes all subscriptions associated with the given event.

        :param event: The DispatcherEvent to unsubscribe from.
        :type event: DispatcherEvent

        :return: True if the subscriptions were successfully removed, raises a ValueError otherwise.
        :rtype: Optional[bool]
        """

        # Check if the event's name exists in the subscriptions
        if event.name not in self._subscriptions:
            # If it does not exist, raise a ValueError
            raise ValueError(f"Event '{event.name}' does not exist.")

        # Unsubscribe all functions associated with the event's name
        del self._subscriptions[event.name]

        # Return to indicate successful unsubscription
        return True

    def unsubscribe_by_function(
        self,
        function: Callable[[Any], Any],
    ) -> Optional[bool]:
        """
        Unsubscribes a function from all events.
        This method removes all subscriptions associated with the given function.

        :param function: The function to be unsubscribed.
        :type function: Callable[[Any], Any]

        :return: True if the subscription was successfully removed, raises a ValueError otherwise.
        :rtype: Optional[bool]
        """

        # Iterate through the subscriptions to find and remove the subscription by function
        for subscription in self._subscriptions.values():
            try:
                subscription.unsubscribe_by_function(function=function)
            except ValueError:
                continue

        # If no matching subscription was found, raise a ValueError
        raise ValueError(f"No subscription found for function '{function.__name__}'.")

    def unsubscribe_by_namespace(
        self,
        namespace: str,
    ) -> Optional[bool]:
        """
        Unsubscribes all functions from a specific namespace.
        This method removes all subscriptions associated with the given namespace.

        :param namespace: The namespace from which to unsubscribe all functions.
        :type namespace: str

        :return: True if the subscriptions were successfully removed, raises a ValueError otherwise.
        :rtype: Optional[bool]
        """

        # Iterate through the subscriptions to find and remove the subscription by namespace
        for subscription in self._subscriptions.values():
            try:
                subscription.unsubscribe_by_namespace(namespace=namespace)
            except ValueError:
                continue

        # Return to indicate successful unsubscription
        return True
