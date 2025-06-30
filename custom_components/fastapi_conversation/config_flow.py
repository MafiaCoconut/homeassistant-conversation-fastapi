"""Config flow for the FastApi Conversation integration."""

from __future__ import annotations

from collections.abc import Mapping
import logging
from typing import Any, cast

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.const import CONF_ENTITY_ID
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import selector
from homeassistant.helpers.schema_config_entry_flow import (
    SchemaConfigFlowHandler,
    SchemaFlowFormStep,
    SchemaFlowMenuStep,
)

from .const import DOMAIN

OPTIONS_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_ENTITY_ID): selector.EntitySelector(
            selector.EntitySelectorConfig(domain=SENSOR_DOMAIN)
        ),
    }
)

CONFIG_SCHEMA = vol.Schema(
    {
        vol.Required("name"): selector.TextSelector(),
    }

).extend(OPTIONS_SCHEMA.schema)

# Параметр отвечающий за появление окошка с конфигурацией при добавлении интеграции
CONFIG_FLOW: dict[str, SchemaFlowFormStep | SchemaFlowMenuStep] = {
    "user": SchemaFlowFormStep(CONFIG_SCHEMA)
}

# Параметр отвечающий за появление окошка с опциональными даннымип при добавлении интеграции
OPTIONS_FLOW: dict[str, SchemaFlowFormStep | SchemaFlowMenuStep] = {
    "init": SchemaFlowFormStep(OPTIONS_SCHEMA)
}

system_logger = logging.getLogger(__name__)


# class ConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
#     """Handle a config or options flow for FastApi Conversation."""

#     config_flow = CONFIG_FLOW
#     # TODOad remove the options_flow if the integration does not have an options flow
#     # options_flow = OPTIONS_FLOW

#     def async_config_entry_title(self, options: Mapping[str, Any]) -> str:
#         """Return config entry title."""
#         system_logger.info("Start function async_config_entry_title in config_flow.py")
#         return cast(str, options["name"]) if "name" in options else ""


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for OpenAI Conversation."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        # if user_input is None:
        #     return self.async_show_form(
        #         step_id="user", data_schema=CONFIG_FLOW
        #     )
        # else:
        user_input = {"key": "value"}
        return self.async_create_entry(
            title="fastapi_agent", data=user_input
        )

        # return self.async_show_form(
        #     step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        # )

