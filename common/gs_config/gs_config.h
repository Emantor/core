// vim : set fileencoding=utf-8 expandtab noai ts=4 sw=4 :
/// @addtogroup common
/// @{
/// @file gs_config.h
/// 
///
/// @date 2013-2014
/// @copyright All rights reserved.
///            Any reproduction, use, distribution or disclosure of this
///            program, without the express, prior written consent of the 
///            authors is strictly prohibited.
/// @author 
///
#include <string>
#include <map>

//class easy_init;

namespace gs {
namespace cnf {
  class gs_config_base : public gs_param_base {
    public:
      explicit gs_config_base(
          const std::string &n, 
          const bool register_at_db = true,
          gs_param_array* parent_array = NULL, 
          const bool force_top_level_name = false) :
        gs_param_base(
          n, 
          register_at_db, 
          parent_array, 
          force_top_level_name) {
      }

      class easy_init {
        public:
          easy_init(gs::cnf::gs_config_base* owner) : m_owner(owner) {}
          ~easy_init() {}

          easy_init& operator()(std::string key, std::string val) {
            m_owner->setProperty(key, val);
            return *this;
          }
          easy_init& operator()(std::string documentation) {
            m_owner->set_documentation(documentation);
            return *this;
          }

        private:
          gs::cnf::gs_config_base* m_owner;
      };

      void setProperty(std::string key, std::string value) {
        m_properties[key] = value;
      }

      std::string getProperty(std::string key) {
        std::map<std::string, std::string>::iterator it;
        it = m_properties.find(key);
        if (it != m_properties.end()) {
          return it->second;
        } else {
          return "Property not found";
        }
      }

      std::map<std::string, std::string> getProperties() {
        std::map<std::string, std::string>::iterator it;
        std::map<std::string, std::string> properties;
        for (it = m_properties.begin(); it != m_properties.end(); ++it) {
          properties[it->first] = it->second;
        }
        return properties;
      }

      void deleteProperty(std::string key) {
        std::map<std::string, std::string>::iterator it;
        it = m_properties.find(key);
        m_properties.erase(it);
      }

      bool exists(std::string key) {
        std::map<std::string, std::string>::iterator it;
        it = m_properties.find(key);
        if (it != m_properties.end()) {
            return true;
         } else {
             return false;
         }
      }

      easy_init add_properties() {
        return easy_init(this);
      }

    private:
      std::map<std::string, std::string> m_properties;
  };
}
}

/// @}
