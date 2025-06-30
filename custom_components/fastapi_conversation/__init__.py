"""The FastApi Conversation integration."""

from __future__ import annotations
import logging


from homeassistant.components import conversation
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers import (
    config_validation as cv,
    entity_registry as er,
    intent,
    template,
)
from .const import DOMAIN
system_logger = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up OpenAI Conversation."""
    await async_setup_services(hass, config)
    return True


# TODOo Remove if the integration does not have an options flow
# async def config_entry_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
#     """Update listener, called when the config entry options are changed."""
#     await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    system_logger.info("Start function async_unload_entry in __init__.py")
    hass.data[DOMAIN].pop(entry.entry_id)
    conversation.async_unset_agent(hass, entry)

    return True


async def async_setup_services(hass: HomeAssistant, entry: ConfigEntry):
    """Set up services for FastApi Conversation."""
    system_logger.info("Start function async_setup_services in __init__.py")


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up FastApi Conversation from a config entry."""
    system_logger.info("Start function async_setup_entry in __init__.py")

    # TODOo Optionally store an object for your platforms to access
    # entry.runtime_data = ...
    # TODOo Optionally validate config entry options before setting up platform
    # await hass.config_entries.async_forward_entry_setups(entry, (Platform.SENSOR,))
    # TODOo Remove if the integration does not have an options flow
    # entry.async_on_unload(entry.add_update_listener(config_entry_update_listener))

    agent = FastApiAgent(hass, entry)
    conversation.async_set_agent(hass, entry, agent)
    data = hass.data.setdefault(DOMAIN, {}).setdefault(entry.entry_id, {})
    data["agent"] = agent

    return True



class FastApiAgent(conversation.AbstractConversationAgent):
    """FastApi Conversation agent."""

    system_logger.info("Start class FastApiAgent in __init__.py")

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize the FastApi Conversation agent."""
        self.hass = hass
        self.entry = entry
        self.histrtory: dict[str, list[dict]] = {}

    @property
    def supported_languages(self) -> list[str]:
        """Return the languages supported by this agent."""
        return ["en"]

    async def query(
            self,
            user_input: conversation.ConversationInput,
            messages,
            exposed_entities,
            n_requests,
    ):
        """Query the FastApi Conversation agent."""
        system_logger.info("query called in FastApiAgent class")

        # Here you would implement the logic to handle the conversation input
        # and return a response. This is just a placeholder implementation.
        system_logger.info(f"User_input context: {user_input.context}")
        system_logger.info(f"User_input conversation_id: {user_input.conversation_id}")
        system_logger.info(f"User_input device_id: {user_input.device_id}")
        system_logger.info(f"User_input language: {user_input.language}")
        system_logger.info(f"User_input agent_id: {user_input.agent_id}")
        system_logger.info(f"User_input extra_system_prompt: {user_input.extra_system_prompt}")
        system_logger.info(f"Messages: {messages}")
        system_logger.info(f"Exposed_entities: {exposed_entities}")
        system_logger.info(f"N_requests: {n_requests}")

        response = {
            "response": "This is a placeholder response.",
            "conversation_id": user_input.conversation_id,
            "messages": messages,
            "exposed_entities": exposed_entities,
        }

    async def async_process(
        self, user_input: conversation.ConversationInput
    ) -> conversation.ConversationResult:
        system_logger.info("async_process called in FastApiAgent class")
        system_logger.info(f"User_input context: {user_input.context}")
        system_logger.info(f"User_input conversation_id: {user_input.conversation_id}")
        system_logger.info(f"User_input device_id: {user_input.device_id}")
        system_logger.info(f"User_input language: {user_input.language}")
        system_logger.info(f"User_input agent_id: {user_input.agent_id}")
        system_logger.info(f"User_input extra_system_prompt: {user_input.extra_system_prompt}")
        intent_response = intent.IntentResponse(language=user_input.language)
        intent_response.async_set_speech(speech="This is a placeholder response.")

        return conversation.ConversationResult(
            response=intent_response, conversation_id=user_input.conversation_id
        )



